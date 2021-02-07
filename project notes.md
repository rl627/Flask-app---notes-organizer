# 1. Set up directory structure

Pretty standard file structure for flask application. 

# 2. create flask application

we set up the python package in __init__.py to import flask and make a funciton which creates a flask application. then in main.py we import that package/function and actually create a flask website. Running will give error because we have not set up any pages or routes for our website. 

# 3. create routes/views

## views.py

We store the standard routes for our website, where users can actually go to (e.g. homepage...). the login page will go into auth.py but any other page that the user can access will be put into views.py. This page is a blueprint which meaning it has a bunch of roots inside of it, it has a bunch of urls defined.  

## auth.py

We also create a blue print here named auth which will serve as the blueprint for the authentication process. 

