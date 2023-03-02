# General Notes as an Extra to the Program

## Venv Environment

### Exporting Installed Packages
Using `virtualenv` - Python integrated virtual environment manager - it's possible to easily save the packages installed in your environment in order to install them in another environment. The command it's needed to type is the following:

> pip freeze > packages.txt

This will save a snapshot of the installed packages in the file named `packages.txt`


### Importing Installed Packages
Still while using `virtualenv`, for importing the packages saved on the file previously created, `packages.txt`, in another, currently activated environment, the following command is needed:

> pip install -r packages.txt

Doing so, now the packages installed via `pip` are available in the second virtual environment, thus the written code runnable in the first virtual environment, is now runnable in the second one too.



# Django Project
Use the following command to create a `django` project:

> django-admin startproject djproject

This creates a `django` project named *djproject*.
Once this is done, enter in the created folder and launch this command in order to @TODO:

> python manage.py startapp myapp

This command creates a new project folder named *myapp*.

# Running Django Project
To render an url, use:

> python .\path\to\project\manage.py runserver

This command will give you an url where it's possible to see the locally created site.