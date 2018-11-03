# Create a Book Review Website

In this project, you’ll build a book review website. 
Users will be able to register for your website and then log in using their username and password. 
Once they log in, they will be able to search for books, leave reviews for individual books, and see the reviews made by other people.

## Preparation

### 1. virtualenv / virtualenvwrapper
Create Environment or Virtual Environment of python=2.7 and activated it
	
### 2. Download the app
After that, download the django-sample-app project files in your workspace:  
	`$ cd /path/to/your/workspace`  
    `$ git clone git://github.com/kirpit/django-sample-app.git projectname && cd projectname`    
	
### 3. Run syntax on cmd
After that run the following syntax:  
	`$ pip install -r requirements.txt`  
	`$ py manage.py makemigrations`  
	`$ py manage.py migrate`  
	`$ py manage.py collectstatic`  
	`$ py manage.py` test # Run the standard tests. These should all pass.    
	`$ py manage.py createsuperuser` # Create a superuser    
	`$ py manage.py runserver 9000`  
	
### 4. Open in the browser
Run this command in your browser:  
	```
	http://127.0.0.1:9000/
	```
