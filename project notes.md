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


# 5. HTTP Requests

## 5.1 Intro

Now that we have our HTML sign up and sign in pages done. We can focus on the backend, what happens when we hit the submit button in our two forms? Right now it displays an error: "Method Not Allowed - The method is not allowed for the requested URL."

This is a a great time to talk about HTTP Requests. We use HTTP (Hyper Text Transfer Protocol).

At any point while we are on our site we are at a route which is a function in either auth.py or view.py. So far everything works, most routes are GET request, which just gets HTML and renders, but once we click a button things break because the clicking of a submit button will create  POST request (as defined in the form ``` <form method = "POST"> </form>```) to the server and respond to us or do something with that post request. Since we have not created much of back end, our server has no idea what to do and just throws an error.

* GET request/method: retrieves information
* POST request/method: updating or creating something
* Other HTTP request: UPDATE, DELETE, PUT

Next stop to fix this is to make sure our server can actually accept this POST request. 

## 5.2 Handling POST Requests

Now since we have two submit buttons, we want to make sure that our login and sign-up routes can accept POST requestions! To do that we need to define something with our routes in auth.py.

```
@auth.route('/login', methods = ['GET','POST'])
@auth.route('/sign-up', methods = ['GET','POST'])
```

By default the routes only accespt GET HTTP request, but now by explicitly specifying the the methods as both GET and POST. Now out login page and sign up pages don't throw errors when we hit submit. TO be specific, when we go to the page via url change that is aa GET request. When we hit the submit button which is within a form that has POST method specified, that is POST request. 

## 5.3 Getting information from HTTP request to server

To get informatino in form into server, first thing is we need to importat the 'request' funciton from flask. Then we add to the route function 

```
def login():
    data = request.form
    print(data)
    return render_template("login.html")
```


We assign the HTTP request information with the attribute form to the variable data then print data. If tehre is no form attribute (e.g. lgoin refresh) there is no data sent but if we hit submitt then we print out the email and password. Using request, the next thing we do is to apply this to the sign-up page and get users info , store that ona  DB and to create user account. 

In the previous example, we did not differential between GET and POST HTTP request, but realistically, we only care about data flow when a submit button or POST request is made. In the sign-up route, we can modify the condition to only collect info when the HTTP request is a GET reqest.

```
@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    return render_template("sign-up.html")
```

In the code above, if the HTTP request is a POST we use the get function to get quite a few pieces of information and store them in variables.

Before we create users let's just make some basic data checks in python to make sure the values are valid.

```
        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif len(password1) != password2:
            pass
        else:
            #add user to database
            pass
```

So before we make user, if this info is not valid we should let the user know! The next section will deal with how to use "message flashing" to alert the users. Before we start looking into databases. 

(1:03:12) https://www.youtube.com/watch?v=dam0GPOAvVI&t=448s&ab_channel=TechWithTim