"""
A composition is a type of relationship between objects where one object is part of another. 
In terms of composition, a "part" cannot exist without a "whole". This means that if the "whole" 
is destroyed or removed, the "part" will also be destroyed or removed.

Composition is effectively used in situations where objects have a strong dependence on each other, 
and the "part" cannot exist without the "whole". That is, if one object owns another object 
and is responsible for its life cycle, then there is a relationship of composition between them.

Let's imagine that we are developing software for project management. 
In this system, each "Project" (Project class) can contain several "Tasks" (Task class),
and these tasks have no meaning outside the context of their project. 
If a project is deleted, all its tasks must also be deleted.
"""

# Let's consider the implementation


class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Task: {self.name}, Description: {self.description}")


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list(Task) = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Project: {self.name}")
        for task in self.tasks:
            task.display_info()


# Creating a project
my_project = Project("Web Development")

# Adding tasks
my_project.add_task("Interface design", "Create main page layout.")
my_project.add_task("API development", "Implement endpoints for users.")

# Display information about the project
my_project.display_project_info()

# Deleting a task
my_project.remove_task("API Development")

# Check for task deletion
my_project.display_project_info()

# Output
# Project: Web development
# Task: Interface design, Description: Create a layout of the main page.
# Task: API development, Description: Implement endpoints for users.
# Project: Web development
# Task: Interface design, Description: Create a layout of the main page.


"""
In this example, the Project class includes objects of the Task class 
as "parts" of the project. Tasks are created and managed exclusively 
through a project, which is a prime example of composition. But why 
is the composition suitable here? The life cycle of Task objects is 
closely related to the life cycle of the Project object. Tasks cannot 
exist without a project. The Project class "owns" its Tasks. This means 
that deleting a project will automatically delete all its tasks.

Composition allows you to encapsulate the behavior and data related to task 
management inside the Project class, making the system more organized and understandable.


Composition is an ideal choice for modeling relationships where there is 
a strong dependency between objects, and the "parts" cannot exist independently 
without the "whole". It provides a clear structure of ownership and management 
of objects, maintaining the integrity and consistency of the system.
"""
