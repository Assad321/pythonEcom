## Live Demo

**Follow this link to view deployed version of the web app http://ecom.southeastasia.cloudapp.azure.com**
**Admin: http://ecom.southeastasia.cloudapp.azure.com/admin**

## Built with 
1. Django
2. Python
2. HTML
3. CSS
4. Bootstrap
5. SQLite database

## Deployment / Hosting

This Project was deployed on Microsoft Azure


## Installation

Follow the below instructions to clone this project for Mac (commands will be slightly different for Windows)

1. Go to folder you want to put the cloned project in your terminal & type:
    `$ git clone https://github.com/Assad321/pythonEcom.git`
2. Create & Activate a new Virtual Environment in terminal:
    Create: `$ python3 -m venv ~/virtualenvs/name_of_environment`
    Activate: `$ source ~/virtualenvs/name_of_environment/bin/activate`
3. Install the project dependancies:
    `$ pip install -r requirements.txt`
4. Create env.sh file at the top level (this will contain all sensitive information)
    **MAKE SURE IT IS IN THE .gitignore FILE**
    
5. In the terminal:
    `$ python manage.py migrate` - this will apply migrations to your local sqlite database
    `$ python manage.py createsuperuser` - this will create admin support
    `$ python manage.py runserver` - should say starting development server..
6. Go to your browser & type '127.0.0.1:8000' in the address bar
7. The App should run on your browser
8. Log in to the admin panel by going to '127.0.0.1:8000/admin' & log in using the credentials you created for the superuser
9. You can add products from here

## Running the tests

Automated tests can be viewed in the tests.py file within the separate Apps. 
To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:

`$ python manage.py test <app name>`
