import sqlite3
from datetime import datetime
from random import choice, randint

import faker

NUMBER_COMPANIES = 3
NUMBER_EMPLOYEES = 30
NUMBER_POST = 5


def generate_fake_data(number_companies, number_employees, number_post):
    fake_companies = []  # here we will store companies
    fake_employees = []  # here we will store employees
    fake_posts = []  # here we will store posts
    """Let's take three faker companies and put them in the desired variable"""
    fake_data = faker.Faker()

    # Let's create a set of companies in number_companies
    for _ in range(number_companies):
        fake_companies.append(fake_data.company())

    # Now generate number_employees number of employees'''
    for _ in range(number_employees):
        fake_employees.append(fake_data.name())

    # And number_post is a set of positions
    for _ in range(number_post):
        fake_posts.append(fake_data.job())

    return fake_companies, fake_employees, fake_posts


def prepare_data(companies, employees, posts):
    for_companies = []
    # prepare a list of tuples of company names
    for company in companies:
        for_companies.append((company,))

    for_employees = []  # for table employees

    for emp in employees:
        """'
        For records in the employee table, we need to add the job title and company id. We had companies by default
        NUMBER_COMPANIES, when creating the companies table for the id field, we specified INTEGER AUTOINCREMENT - therefore each
        the record will receive a consecutive number increased by 1, starting from 1. Therefore, the company is chosen randomly
        in this range
        """
        for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))

    """'
    We will perform similar operations in the payments table of salary payments. Let's assume that all companies pay salaries
     performed from the 10th to the 20th of each month. We will generate a salary range from 1,000 to 10,000 u.o.
     for each month and each employee.
     """
    for_payments = []

    for month in range(1, 12 + 1):
        # We execute the cycle by months'''
        payment_date = datetime(2021, month, randint(10, 20)).date()
        for emp in range(1, NUMBER_EMPLOYEES + 1):
            # We execute the cycle according to the number of employees
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments


def insert_data_to_db(companies, employees, payments) -> None:
    # Let's create a connection with our database and get a cursor object for data manipulation

    with sqlite3.connect("salary.db") as con:

        cur = con.cursor()

        """Filling in the table of companies. And we create a script for insertion, where we will note the variables that we will insert
         placeholder (?) """

        sql_to_companies = """INSERT INTO companies(company_name)
                                VALUES (?)"""

        """To insert all data at once, use the executemany cursor method. The first parameter will be the text
         script, and the second - data (a list of tuples)."""

        cur.executemany(sql_to_companies, companies)

        # Next, we insert data about employees. Let's write a script for it and specify the variables

        sql_to_employees = """INSERT INTO employees(employee, post, company_id)
                                VALUES (?, ?, ?)"""

        # The data has been prepared in advance, so we just pass it to the function

        cur.executemany(sql_to_employees, employees)

        # Last, we fill in the table with salaries

        sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
                               VALUES (?, ?, ?)"""

        # Insert salary data

        cur.executemany(sql_to_payments, payments)

        # We record our changes in the database

        con.commit()


if __name__ == "__main__":
    companies, employees, posts = prepare_data(
        *generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYEES, NUMBER_POST)
    )
    insert_data_to_db(companies, employees, posts)
