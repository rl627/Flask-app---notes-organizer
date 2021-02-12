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

## 4.1 base.html

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

To break this down: whenever we have ``` {{  }} ``` it means that ther e some python extpression (variable,expression, funciton) inside that will be evaluated. In this case we call the funciton url_for() which will find the url for our js file and return this as a string to the src argument. 

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
Now that we have created our template, now we need to actually define some HTML documents that actually use this template. Yes, we can render this template but the ploint of a tmeplate is to use it as base for other pages in our website. This is what we will do next and create a home.html using base.html. 

## 4.2 Extending base.html and rendering child templates



### Extend base.html and render

The first thing we do is to indicate that this template is an extension of home.html by add the following ot the top of page. THen we can use our block fnuction to override the title of our page. For now we will overirde with Home2, so we can see the difference. 

```
{% extends "base.html" %} 
{% block title %}Home2{% endblock %} 
```


The next key step now that we have extended base.html tempalte with home.html is to render this child in our website. We go to views.py which is the file that defines all the non-auth pages of website and import another funciton from flask which renders template, then use this functiont o call our child template to render

```
@views.route('/')  
def home():
    return render_template("home.html")
```

### Add content block to base.html

Indeed it works! The next step is to insert a block into our base.html which we can put content on the screen. In the code below, we put the content in a container class which is the most basic layout element that keeps things floating away from edges. 

```
<div class="container">{% block content %} {% endblock %}</div>
```

Then by adding to the block name content in the child template will overirde this and display stuff when the child is rendered. For example into, home.html we can add the following: 

```
{% block content %}
<h1>THIS IS THE HOME PAGE</h1>
{% endblock %} 
```

We can repeat this to create child templates for all our other pages. THen render them in auth.py.

## 4.3 Passing values between templates

One of the great things that is great about this jinja templating language is that we can pass variables or values to all of the templates and that will allow us to use those values inside of those templates. For a first example, we can pass a variable to login.html on our backend (auth.py) by naming a variablea nd giving it a value:

```
render_template("login.html", text = "testing")
```

In this way we can access the varible text inside of login.html. with ```{{text}} ```

This is how we pass values to our templates, we simply define them as some variable. We can also pass multiple variables. One useful use of this is if we pass a boolean and then use an conditional in out tempalte. 

```
render_template("login.html", text = "testing", boolean = True)
```

Then in the template.

```
{% if boolean == True %}
Yes it is true!
{% else %}
No it is not true!
{% endif %}
```

we can do a bunch of conditions such as elif or for loops. 


## 4.4 Develop the sign-up.html and login.html pages


Lest do this so we can allow users to sign up and start working on the backend and working with databases... and other fun stuff. This is all done in bootstrap, relatively straight forward.

The on new thing is when we are creating the for tag we use POST as the method, which we will learn about later. 

```
 <form method = "POST"></form>
```


# 5. Handling the Form


(54:17) https://www.youtube.com/watch?v=dam0GPOAvVI&t=448s&ab_channel=TechWithTim