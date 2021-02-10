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

# 4. Jinja Templating Language & HTML Templates

Right now the pages that we have created and registered routes for (home, login, logout, signup) have just simple HTML which is a function. But typing HTML like this isn't scalable. Now we will build templates into to the >website>templates with Jinja, which is python's version of a templating engine (this allows some templating functionality which is usually in javascript to be done in python).

## base.html

The first template we create is 'base.html' which is kind of like the theme of our website. What ever is in this template is what the entire site will look like .. (e.g. navbar, footer, header ...). Then what we will do is to overide parts of the base.html with more specific templates. 

### Head 

import bootstrap and define title tag with Jinja. ```{% %}``` acts like a chunk in which python code can be inserted. In this case we will insert python  block end block (```{% block title%}Home{% endblock %}```) which says that any blocks that we have defined in this base template which in this case is title will be inherited by children template and can be overided/changed. 



### Body

#### Scripts

We load some javascript that supplements bootstrap (animations and.... etc). This i always at the bottom ot he body. Things that don't chnage go into static (images, javascript, css).  If we wanted to write own javascript, then we would write a javascript file into the static folder and load with this code 

```   
<script 
    type="text/javascript" 
    src="{{ url_for('static', filename='index.js') }}"
></script>
```

To break this down: whenever we have ``` {{  } ``` it means that ther e some python extpression (variable,expression, funciton) inside that will be evaluated. In this case we call the funciton url_for() which will find the url for our js file and return this as a string to the src argument. 

#### navbar

We will just define a bootstrap navbar class. 

```
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
</nav>
```

Then we will add buttons to navbar. First one is if our screen is small (e.g. mobile device) and we cannot see all buttons then we expand so we see all the buttons. The icon we see is the icon in the middle.

```
<button class="navbar-toggler" type="button" data-toggle="collapse"data-target="#navbar">
      <span class="navbar-toggler-icon"></span>
</button>
```

Next we will create out navbar. The code creates a navbar that is collabsable with id navbar. 

```
  <div class="collapse navbar-collapse" id="navbar">
  </div>
```

Next we insert items in our navbar into another div as shown below. 

```
  <div class="collapse navbar-collapse" id="navbar">
   <div class="navbar-nav">
       <!-- INSERT ITEMS -->
    </div>
  </div>
```

Lets add some pages!

```
<div class="collapse navbar-collapse" id="navbar">
        <div class="navbar-nav">
          <a class="nav-item nav-link" id="home" href="/">Home</a>
          <a class="nav-item nav-link" id="logout" href="/logout">Logout</a>
          <a class="nav-item nav-link" id="login" href="/login">Login</a>
          <a class="nav-item nav-link" id="signUp" href="/sign-up">Sign Up</a>
        </div>
      </div>
```

