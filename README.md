
# Hardware Store
 ## Backend development



## Contents.

* ### [User Experience](#user) (UX)

 * [Project Goals](#Pro)
 * [Developer and Business Goals](#Dev)
 
 
*  ### [Design](#Des)

 * [font styles used](#Font)
 * [Colours and background images](#colour)
 * [Features](#Feat)


* ### [Technologies Used](#Tech)

 * [Languages Used](#Lang)
 * [Frameworks, Libraries & Programs Used](#Frame)
  
* ### [Deployment](#Deploy)

* [Local Deployment](#Local)

  
* ### [Testing](#Test)

 * [W3 Nu HTML Validator](#w3-NU-HTML)
 * [Manual Testing](#Man-Test)
 * [Bugs](#Bugs)
 * [Development of website](#Development)
   
* ### [Credits](#Credits)
 

 * [Authors](#Auth)
 * [Acknowledgements](#Acknow)



<a name="user"></a>
 ### User Experience (UX)

<a name="Pro"></a>
 * ### Project Goals

The project Goal is to create a backend developed database for a hardware store selecting the categories of hardware supplied coupled with an Items page to provide which items and which date they are required for.
This would link into a website that woould show a gallery of photos for the products available and also a payment page that can be used once the customer is happy with there selection.




<a name="Dev"></a>
### Developer Business and Goals.


<img width="750" alt="main screenshot" src="https://live.staticflickr.com/65535/53298173743_d249dcc7ed_z.jpg">

<br><br>


The "Home. page", is a basic site that allows the use to choose items to add or categories to choose from.
The "add Items" page (as shown in the sceen shot above allows the use to select items fo purchasing.
The "categories" page allows the customer to update and delete the categories as required.


<a name="User"></a>
### User Stories

As this is a backend develope site with a font end display it is more to allow the custome a selection of projects that would be attached to a fully fuctional site to search and then purchase hardware from the supplier.


<a name="Des"></a>
## Design

The design is based on the 'code institute' task manager backend developement learning page.

<a name="Font"></a>
### Font styles used

TBC


<a name="Colour"></a>
### Colours and background images.

The colours are based on the Venezuelan flag. The background drop is the factory in connection that will supply the hardware.

<a name="Feat"></a>
### Features

The features are a home page showing the basic options, an Items selection page where the user can choose the items, then an item description allowing to put more information in. A due date for the items required. An urgent lever to select its an urgent purchase and a category selection to see if the product is available.

There is a category selection where in hind-site should only be allowed to be updated by the vendor but, due to real life issues and getting the database and python to function it has been left to function as dual entity which I appreciate is not viable if it was the finished article. This allows the choice of hardware to be selected via the categories populated. if it was managed by staff they could delete a product if wasn't available or add once it became available.

<a name="Deploy"></a>
### Deployment.


To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 run.py`, if your Python file is named `run.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Open up the more selection button.
3. open run console
4. Type Python3
5. Then type "from hardware import db"
6. "db.create_all()
7. "exit()
8. Select open app


<a name="Local"></a>
### Local Deployment
[A link to GitHub] (https://github.com/Sniffy2019/Hardware-store)

Using code anywhere or Gitpod; and using the terminal $ python3 -m http.server
then using port 5000 will show the web page.


<a name="Tech"></a>
### Technologies used

## Sources:
Code institute LMS



<a name="Frame"></a>
### Frameworks, Libraries & Programs Used

* cdnjs.cloudflare.com/ajax/libs/hover.css/2.1.1/css/hover-min.css
* cdn.jsdeliver.net
* code.jquery.com/jquery-3.6.0.min.js
* js.stripe.com/v3/
* live.staticflickr.com
* cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css
* maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css
  

<a name="Lang"></a>
### Languages used

* Html
* CSS
* Javascript
* python
  


<a name="Test"></a>
### Testing


### Automated Testing

* Tests have been run on Code anywhere
Using Html, CSS and Python



* Glitch was used to format the code in Html  files.
* Checked via glitch for presentation.
  
<a name="w3-NU-HTML"></a>
* W3C was used to eliminate any glaring errors and conflicts on the web pages.
* Main index.html, assets/html NU HTML checker
[HTML Link](https://live.staticflickr.com/65535/53023596177_6a3bcd1ef2_z.jpg)
[HTML Link 1](https://live.staticflickr.com/65535/53024659358_602b0ef0a9_c.jpg)
[HTML link 2](https://live.staticflickr.com/65535/53024372984_d4bb32bfe6_z.jpg)
[HTML link 3](https://live.staticflickr.com/65535/53036416374_c370055684_b.jpg)



<a name="Man-Test"></a>
### Manual Testing


For the database creation other than the table.py page.
first iniate psql on the bash commmand line
* CREATE DATABASE hardware;
* \c hardware;
* \q

This should have created the table in Flask-SQLAlchemy

for Python
* from hardware import db
* db.create_all()
* exit()

  I had to use gitpod (gp) init -i, then gitpod (gp) validate to get the SQL to work.

  Which is why the gitpod.yml is in this file.

  If I had not loaded this this the psql on the bash script would not activate; this would have killed the table data.
  









<a name="Bugs"></a>
### Glitches/Bugs

The pages and links have been tested, and the buttons react well.

There has been some errors with the linking software; especially psycopg2 and the table functioning to accept input data.
Also before I managed to get heroku to work; if you made a double/repeated input on the Add Items page it would crash the site.

<a name="development"></a>
### Development



<a name="video"></a>
### Media



<a name="Auth"></a>
### Authors

Code Institute-initial-work Alex Parry



<a name="Acknow"></a>
### Acknowledgments

*Code Institute:- base layout of website and code to create the front page.


*Robert Mclaughlin:- For reviewing ideas.



