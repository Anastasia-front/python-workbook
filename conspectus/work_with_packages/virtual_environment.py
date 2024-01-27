# Using pip involves executing it as a Python script with arguments when called.
# For example, to display a list of installed packages:

# python -m pip list / python3 -m pip list


"""The -m value indicates that the package should be invoked 
as an executable script, list is the argument that pip "understands" 
what to do (list the installed packages). The output will be similar 
to this, but will differ because different computers have their own set of installed packages.
"""

# Installing of packages
latest_version = "pip install requests"

specific_version = "pip install requests==2.28.2"

package_newer_than = "pip install requests>=2.28.2"

package_earlier_than = "pip install requests<=2.28.2"

removing = "pip uninstall requests"

list_of_installed_packages_with_versions = "pip freeze"


"""A virtual environment is an isolated environment for Python projects. 
By using a virtual environment, you can install libraries and their 
dependencies within that environment without affecting the global 
Python environment or other virtual environments.

There are many tools that automate the creation/deletion/activation 
of a virtual environment for us. The simplest and most standard tool is venv.

You can read what venv can do on the official documentation page. 
Like pip, venv is Python's built-in console script.



To create a new virtual environment, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to create your Python project.
3. Run the following command to create a virtual environment:
"""

first_step = "python -m venv .venv /python3 -m venv .venv"

"""
This will create a .venv directory in the current directory 
that will contain the virtual environment.

After running this command, Python with a minimal set 
of standard packages will be copied to the .venv directory. 
And you will be able to use this Python separately from 
the main system one or any other.

To start using Python from a virtual environment, 
activate the virtual environment. To activate the virtual environment, 
use one of the following commands, depending on your system and shell:
"""

# On Windows in the command line (CMD):
second_step = ".\.venv\Scripts\activate.bat"

# On Windows in PowerShell:
second_step = ".\.venv\Scripts\Activate.ps1"

# On macOS and Linux:
second_step = "source .venv/bin/activate"

"""
Once activated, the command prompt will change to display 
the name of the virtual environment, indicating that it is active.

For example, for PowerShell under Windows, executing the command:
"""
# PS E:\example_joke> .\.venv\Scripts\Activate.ps1


"""Activates the virtual environment and the console changes to the following:
"""

# (.venv) PS E:\example_joke>

"""
As you can see, we are told (.venv) that we are now in a 
virtual environment located in the .venv directory.
Now, after activation in this console, the python call 
will not call the system Python, but the version from 
the .venv directory with its packages.

After enabling the virtual environment, you can install/remove 
packages using pip in the virtual environment. Installing/removing 
packages affects only the virtual environment and 
does not affect the system or other projects."""

# To install the necessary libraries within this virtual environment, use pip install:
third_step = "pip install package_name"


"""These installed libraries will be isolated from the global Python environment."""

# To switch back to system Python, run in the console:
switch_back = "deactivate"

"""
This will return you to the global Python environment.

To remove a virtual environment, it is enough to 
physically delete the .venv directory with all 
its contents in the project directory.



Using venv is a standard practice for creating isolated 
environments for Python projects, which avoids conflicts 
between dependencies of different projects. This keeps your 
work environment clean and simplifies library and dependency management."""
