from datetime import datetime

import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime

Parsing = """is the most common way to retrieve data from the Internet for various types of applications. 
The practically infinite amount of information in the network explains the existence of various tools for its collection. 
In the process of scraping, the computer sends a request, in response to which it receives an HTML document. 
After that, the parsing stage begins. Here you can focus only on the data you need. Consider parsing using libraries such as Beautiful Soup, Ixml, and Requests.
"""

# Beautiful Soup Basics
"""Installing the necessary packages:

pip install lxml
pip install requests
pip install beautifulsoup4"""

# Where to start scraping
"""To familiarize yourself with the scraping process, you can use the site https://quotes.toscrape.com/, 
which was created just for this. It could be used to create, for example, a repository of author names, tags, or quotes themselves."""


# Automation of obtaining "raw" data
"""
To begin with, we import the necessary packages, make a request using requests, and in response we will receive the HTML page 
we are looking for. Next, let's convert the response from the server into lxml format and pass the result to BeautifulSoup for processing.
"""

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

print("\n" + "~" * 30 + "\n")
print(soup)
print("\n" + "~" * 30 + "\n")

# <!DOCTYPEhtml>
# <html lang="en">
#    <head>
#      <meta charset="utf-8" />
#      <title>Quotes to Scrape</title>
#      <link href="/static/bootstrap.min.css" rel="stylesheet" />
#      <link href="/static/main.css" rel="stylesheet" />
#    </head>
#    <body>
#      <div class="container">
#        <div class="row header-box">
#          <div class="col-md-8">
#            <h1>
#              <a href="/" style="text-decoration: none">Quotes to Scrape</a>
#              ...
#            </h1>
#          </div>
#        </div>
#      </div>
#    </body>
# </html>


"""
In the console, you will see the code of the site page without indents, but broken down by tags so that each tag is on a separate line.

It is not necessary to use Lxml, BeautifulSoup can work with "pure" HTML, but the Lxml library can speed up processing a little.

Next, you need to find some template in the browser, according to which you can get only the necessary data.
"""

"""---------------------------------------------------------------------"""


# Parsing HTML

# Search on the page by tag, by class, by ID

"""An HTML document stores a lot of information, but with Beautiful Soup, it's easier to find the data you need. 
Sometimes it only takes one line of code. Let's try to find all span tags with the text class. 
This, in turn, will return all tags. When you need to find several identical tags, you should use the find_all() function.
"""
# REPEAT:
# import requests
# from bs4 import BeautifulSoup
# url = '<https://quotes.toscrape.com/>'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all("span", class_="text")

print(quotes)
print("\n" + "~" * 30 + "\n")

# [<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>, <span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.” </span>, <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>, <span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>, <span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”</span>, <span class ="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>, <span class="text" itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</ span>, <span class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>, <span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>, <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span> ]


"""Recursive markup isn't exactly what's needed. To get only data - quotes in this case, you can use the .text property.
"""
# REPEAT

for quote in quotes:
    print(quote.text)
print("\n" + "~" * 30 + "\n")

# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# “It is our choices, Harry, that show what we truly are, far more than our abilities.”
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
# “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
# “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
# “Try not to become a man of success. Rather become a man of value.”
# “It is better to be hated for what you are than to be loved for what you are not.”
# “I have not failed. I've just found 10,000 ways that won't work.”
# “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
# “A day without sunshine is like, you know, night.”


"""To search and display all authors, we work according to the same principle — first you need to manually study the page. 
You can pay attention to the fact that each author is included in the <small> tag with the author class. 
Next, we use the find_all() function and store the result in the authors variable.
"""
# REPEAT
quotes = soup.find_all("small", class_="author")

for quote in quotes:
    print(quote.text)
print("\n" + "~" * 30 + "\n")

# Albert Einstein
# J.K. Rowling
# Albert Einstein
# Jane Austen
# Marilyn Monroe
# Albert Einstein
# André Gide
# Thomas A. Edison
# Eleanor Roosevelt
# Steve Martin


"""
Let's add the code to get all the tags for each quote. First, you need to get each outer block of each tag collection. 
If this first step is not performed, the tags can be retrieved, but not associated with a specific quote.

When a block is obtained, it is possible to drill down using the find_all function for the obtained subset. 
And then you will need to add an inner loop to complete the process.
"""
# REPEAT
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print("--" + authors[i].text)
    tagsforquote = tags[i].find_all("a", class_="tag")
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    break
print("\n" + "~" * 30 + "\n")

# "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
# --Albert Einstein
# change
# deep-thoughts
# thinking
# world


"""
In this example, we exit the quote processing loop after the first quote using break. If you want to get all quotes from this page, comment out break.

Another good resource for learning scraping is [http://scrapingclub.com.](http://scrapingclub.com./) There are tons of tutorials on using another, more advanced tool, Scrapy.
"""


# Search items
"""We systematize the information obtained from the search for elements on the web page.
"""

#  IMPORTS
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

"""As you can see, Beautiful Soup allows you to search for elements on a page using various methods.
For example, you can use the find method to find the first occurrence of an element on a page:
"""

# find the first <p> tag on the page
first_paragraph = soup.find("p")

"""Inside the first_paragraph variable will be the following html element:
"""
# <p>
#      <a href="/login">Login</a>
# </p>

"""You can also use the familiar find_all method to find all occurrences of an element on a page:
"""
# find all <p> tags on the page
all_paragraphs = soup.find_all("p")


"""Inside the all_paragraphs variable will be a list of the following html elements:
"""
# [<p>
#      <a href="/login">Login</a>
# </p>
# <p class="text-muted">
#      Quotes by: <a href="<https://www.goodreads.com/quotes>">GoodReads.com</a>
# </p>
# <p class="copyright">
#      Made with <span class="sh-red">❤</span> by <a href="<https://scrapinghub.com>">Scrapinghub</a>
# </p>]


"""---------------------------------------------------------------------"""


# Work with the content of elements


"""Beautiful Soup allows you to access the content of elements on a page. In addition to using the text attribute, you can get the text of an element using the get_text method:
"""
# get the text of the first <p> tag on the page
first_paragraph_text = first_paragraph.get_text()
print(first_paragraph_text.strip())  # 'Login'
print("\n" + "~" * 30 + "\n")


"""You can also access element attributes using regular Python syntax:
"""
# get the value of the "href" attribute of the first <a> tag on the page
first_link = soup.find("a")
first_link_href = first_link["href"]
print(first_link_href)  # '/'
print("\n" + "~" * 30 + "\n")


"""---------------------------------------------------------------------"""


# Document navigation

"""Beautiful Soup lets you do document navigation and access parent and child elements.
"""

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Child elements
"""To get all child elements of the first <body> tag on the page, use the children attribute.
"""
body_children = list(first_paragraph.children)
print(body_children)
print("\n" + "~" * 30 + "\n")

# ['\\n', <a href="/login">Login</a>, '\\n']


"""We can use chains of find method calls.
"""
# find the first <a> tag inside the first <div> tag on the page
first_div = soup.find("div")
first_div_link = first_div.find("a")
print(first_div_link)
print("\n" + "~" * 30 + "\n")

# <a href="/" style="text-decoration: none">Quotes to Scrape</a>

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Parental elements
"""To get the parent element of the first <p> tag on the page, we can use the parent property
"""
first_paragraph_parent = first_paragraph.parent
print(first_paragraph_parent)
print("\n" + "~" * 30 + "\n")

# <div class="col-md-4">
#      <p>
#          <a href="/login">Login</a>
#      </p>
# </div>


"""You can also use the find_parent and find_parents methods to find parent elements:
"""
container = soup.find("div", attrs={"class": "quote"}).find_parent(
    "div", class_="col-md-8"
)
print(container)
print("\n" + "~" * 30 + "\n")

# We will skip the full derivation due to its large volume:
# <div class="col-md-8">
#      <div class="quote" itemscope="" itemtype="<http://schema.org/CreativeWork>">
#          <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
#          <span>by <small class="author" itemprop="author">Albert Einstein</small>
# <a href="/author/Albert-Einstein">(about)</a>
# </span>
#          ...


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Neighboring elements


"""
You can access neighboring elements using the next_sibling and previous_sibling attributes.

For example, to get the next adjacent element of the first <span> tag with class "tag-item" on the page:
"""

next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
print(next_sibling)
print("\n" + "~" * 30 + "\n")

# <span class="tag-item">
#      <a class="tag" href="/tag/inspirational/" style="font-size: 26px">inspirational</a>
# </span>

"""To get the previous neighboring element of the first <span> tag with class "tag-item" on the page:
"""
previous_sibling = next_sibling.find_previous_sibling("span")
print(previous_sibling)
print("\n" + "~" * 30 + "\n")

# <span class="tag-item">
#      <a class="tag" href="/tag/love/" style="font-size: 28px">love</a>
# </span>

"""---------------------------------------------------------------------"""


# Search by CSS selectors

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Simple selectors


"""
Simple selectors search for elements by tag name, class, or ID using the select method. 
The select method allows you to search for elements based on CSS selectors. 
It takes a string with a CSS selector and returns all elements matching that selector.

Let's find all the <p> tags on the page
"""
p = soup.select("p")
print(p)
print("\n" + "~" * 30 + "\n")

# [<p>
#      <a href="/login">Login</a>
# </p>, <p class="text-muted">
#      Quotes by: <a href="<https://www.goodreads.com/quotes>">GoodReads.com</a>
# </p>, <p class="copyright">
#      Made with <span class="sh-red">❤</span> by <a href="<https://scrapinghub.com>">Scrapinghub</a>
# </p>]


"""Let's find all elements with the class "text"
"""
text = soup.select(".text")
print(text)
print("\n" + "~" * 30 + "\n")

# [<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>,
# <span class="text"
#        itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>,
# <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>,
# <span class="text" itemprop="text">“The person, be it gentleman or lady, who has no pleasure in a good novel, must be intolerably stupid.”</span>,
# <span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”</span>,
# <span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>, <span
#          class="text"
#          itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>, <span
#          class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>, <span
#          class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>,
# <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>]


"""Let's find all the elements with the identifier "header". An identifier is a special attribute of the id tag.
"""
header = soup.select("#header")
print(header)
print("\n" + "~" * 30 + "\n")

# As you can see, such elements do not exist and we get an empty list.
# []

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Combined selectors


"""Combined selectors search for elements that meet multiple conditions.
For example, we will find all the <a> elements inside the <div> tag with the class "container":
"""


a = soup.select("div.container a")
print(a)
print("\n" + "~" * 30 + "\n")

# [<a href="/" style="text-decoration: none">Quotes to Scrape</a>, <a href="/login">Login</a>, <a
#          href="/author/Albert-Einstein">(about)</a>, <a class="tag" href="/tag/change/page/1/">change</a>, <a class= tag
#                                                                                                               href="/tag/deep-thoughts/page/1/">deep-thoughts</a>,
# <a class="tag" href="/tag/thinking/page/1/">thinking</a>, <a class="tag" href="/tag/world/page/1/">world< /a>, <a
#          href="/author/J-K-Rowling">(about)</a>, <a class="tag" href="/tag/abilities/page/1/">abilities</a>, <a
#          class="tag" href="/tag/choices/page/1/">choices</a>, <a href="/author/Albert-Einstein">(about)</a>, <a
#          class="tag" href="/tag/inspirational/page/1/">inspirational</a>, <a class="tag"
#                                                                              href="/tag/life/page/1/">life</a>, <a
#          class="tag" href="/tag/live/page/1/">live</a>, <a class="tag" href="/tag/miracle/page/1/">miracle</a >, <a
#          class="tag" href="/tag/miracles/page/1/">miracles</a>, <a href="/author/Jane-Austen">(about)</a>, ....... <a
#          href="<https://www.goodreads.com/quotes>">GoodReads.com</a>, <a href="<https://scrapinghub.com>">Scrapinghub</a>]


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Attributes


"""You can search for items by attribute value. Find all elements whose href attribute begins with "https://"
"""
href = soup.select("[href^='https://']")
print(href)
print("\n" + "~" * 30 + "\n")

# [<a href="<https://www.goodreads.com/quotes>">GoodReads.com</a>, <a href="<https://scrapinghub.com>">Scrapinghub</a> ]


"""Let's find all the elements in which the class attribute contains the word "text":
"""
text = soup.select("[class*='text']")
print(text)
print("\n" + "~" * 30 + "\n")

# [<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>,
# <span class="text"
#        itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>,
# <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>,
# <span class="text" itemprop="text">“The person, be it gentleman or lady, who has no pleasure in a good novel, must be intolerably stupid.”</span>,
# <span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”</span>,
# <span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>, <span
#          class="text"
#          itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>, <span
#          class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>, <span
#          class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>,
# <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>, <p class="text-muted">
#      Quotes by: <a href="<https://www.goodreads.com/quotes>">GoodReads.com</a>
# </p>]


"""---------------------------------------------------------------------"""

# SUMMARY

"""The choice between the select method and the find method depends on your preferences, level of knowledge of CSS selectors, 
and requirements for finding elements. If you are more comfortable with CSS selectors and need to perform complex queries, 
then select is the better choice. If you just need to find the first matching element, then find might be a more convenient option.
"""


# A practical example

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Project preparation

"""
In a practical example, we will parse the site http://books.toscrape.com/, which was created specifically for this.

First of all, let's create a virtual poetry environment. 

Next, install the necessary Beautiful Soup package:

poetry add beautifulsoup4

We will use the [requests](<https://requests.readthedocs.io/en/master/>) package for HTTP requests.

poetry add requests

And to save the results in the database, we use [SQLAlchemy](<https://www.sqlalchemy.org/>).

poetry add sqlalchemy

We will immediately provide the complete code of our project, and then we will analyze how it works. The main.py file
"""

"""
First, we import the required modules and model to save the data.

The file for the data model model.py has the following structure:
"""


# from datetime import datetime

# from sqlalchemy import Column, Float, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    img_url = Column(String(250), nullable=False)
    rating = Column(Integer, nullable=False)
    title = Column(String(150), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    created = Column(DateTime, default=datetime.now())


# import requests
# from bs4 import BeautifulSoup
# from sqlalchemy.engine import create_engine
# from sqlalchemy.orm import sessionmaker

# from model import Book, Base


def parse_data():
    rate_to_number = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    url = "http://books.toscrape.com/"
    store_ = []
    html_doc = requests.get(url)

    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.content, "html.parser")
        books = soup.select("section")[0].find_all(
            "article", attrs={"class": "product_pod"}
        )
        for book in books:
            img_url = f"{url}{book.find('img')('src')}"
            rating = rate_to_number.get(
                book.find("p", attrs={"class": "star-rating"})["class"][1]
            )
            title = book.find("h3").find("a")["title"]
            price = float(book.find("p", attrs={"class": "price_color"}).text[1:])
            store_.append(
                {"img_url": img_url, "rating": rating, "title": title, "price": price}
            )

    return store_


if __name__ == "__main__":
    store = parse_data()
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    for el in store:
        book = Book(
            img_url=el.get("img_url"),
            rating=el.get("rating"),
            title=el.get("title"),
            price=el.get("price"),
        )
        session.add(book)
    session.commit()
    books = session.query(Book).all()
    for b in books:
        print(vars(b))
    session.close()
print("\n" + "~" * 30 + "\n")


"""The card code is as follows."""


# <article class="product_pod">
#    <div class="image_container">
#      <a href="catalogue/a-light-in-the-attic_1000/index.html"
#        ><img
#          src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
#          alt="A Light in the Attic"
#          class="thumbnail"
#      /></a>
#    </div>

#    <p class="star-rating Three">
#      <i class="icon-star"></i>
#      <i class="icon-star"></i>
#      <i class="icon-star"></i>
#      <i class="icon-star"></i>
#      <i class="icon-star"></i>
#    </p>

#    <h3>
#      <a
#        href="catalogue/a-light-in-the-attic_1000/index.html"
#        title="A Light in the Attic"
#        >A Light in the ...</a
#      >
#    </h3>

#    <div class="product_price">
#      <p class="price_color">£51.77</p>

#      <p class="instock availability">
#        <i class="icon-ok"></i>

#        In stock
#      </p>

#      <form>
#        <button
#          type="submit"
#          class="btn btn-primary btn-block"
#          data-loading-text="Adding..."
#        >
#          Add to basket
#        </button>
#      </form>
#    </div>
# </article>


"""
A cursory analysis says that the book cover is in the img thesis, and the book title is in the title field in the a thesis. 
We also see the rating of the book in class class="star-rating Three" of tag p and its price in thesis p with class price_color.


We receive data for the book:
For this we have parse_data function.

Define url = '<http://books.toscrape.com/'> for the request. The store_ variable, where we will store the received data. 
And we make a request to the site html_doc=requests.get(url).

If the result is successful and the response code is 200, we start extracting data from the HTML code.

Parsing data from HTML code.
soup = BeautifulSoup(html_doc.content, 'html.parser')
We find all the books with the following query.
books = soup.select('section')[0].find_all('article', attrs={'class': 'product_pod'})


And further in the cycle, we begin to get information from the card of each book.
We get the book cover from the src attribute of the img tag.
img_url = f"{url}{book.find('img')('src')}"

It is worth noting that the path to the book cover inside the src tag is relative media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg. 
For it to be functional, it must be converted to an absolute path. To do this, you need to substitute the value of the url variable at the beginning of the path.

The book rating is found as the class name in the thesis p.
<p class="star-rating Three">
   <i class="icon-star"></i>
   <i class="icon-star"></i>
   <i class="icon-star"></i>
   <i class="icon-star"></i>
   <i class="icon-star"></i>
</p>

But it is better to store the numerical value of the rating in the database (DB). For this we introduced a dictionary
rate_to_number = {
     'One': 1,
     'Two': 2,
     'Three': 3,
     'Four': 4,
     'Five': 5
}

Which will convert the class name into a number:
rating = rate_to_number.get(book.find('p', attrs={'class': 'star-rating'})['class'][1])

It is worth noting that the expression book.find('p', attrs={'class': 'star-rating'})['class'] will return us 
a list ['star-rating', 'Three'] , where we need only the second class of element.

We get the title of the book from the title attribute of the a tag:
title = book.find('h3').find('a')['title']

Since there are two a tags inside the book card, we specify the search.

And last we get the price of the book:
price = float(book.find('p', attrs={'class': 'price_color'}).text.removeprefix('£'))

We remove the £ prefix from the price and reduce it to a number.

The last stage - we place the dictionary with book data in the store_ list:
store_.append({
     'img_url': img_url,
     'rating': rating,
     'title': title,
     'price': price
})


We put the data in the database:
After performing all actions, we get a store list with data about books. We put this data in the database.

if __name__ == '__main__':
     store = parse_data()
     engine = create_engine("sqlite:///my_books.db")
     Base.metadata.create_all(engine)
     Base.metadata.bind = engine
     Session = sessionmaker(bind=engine)
     session = Session()
     for el in store:
         book = Book(img_url=el.get('img_url'), rating=el.get('rating'), title=el.get('title'), price=el.get('price'))
         session.add(book)
     session.commit()
     books = session.query(Book).all()
     for b in books:
         print(vars(b))
     session.close()


If you did everything without errors, you will get an in-memory SQLite database with book data.

If we query the books table in the database, we will get a list of books.

SELECT * FROM books LIMIT 5

In this practical example, we parsed an HTML page. Got the data from the HTML code and put it in the database."""
