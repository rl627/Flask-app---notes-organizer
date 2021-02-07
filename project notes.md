# 1. Set up directory structure

Pretty standard file structure for flask application. 

# 2. create flask application

we set up the python package in __init__.py to import flask and make a funciton which creates a flask application. then in main.py we import that package/function and actually create a flask website. Running will give error because we have not set up any pages or routes for our website. 

# 3. create routes/views

## Creating Blueprints and Views

We store the standard routes for our website in views.py, where users can actually go to (e.g. homepage...). the login page will go into auth.py but any other page that the user can access will be put into views.py. This page is a blueprint which meaning it has a bunch of roots inside of it, it has a bunch of urls defined.  

We add 'pages' to the blue print which consist of two parts a decorator whichs specifies route and a funciton which returns content (e.g. HTML code)

## Register blueprints in __init__.py

Now that we have created the routes, we need to import and register these new routes to the web app in the __init__.py file. 