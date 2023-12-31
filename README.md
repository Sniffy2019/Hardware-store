
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
 * [Future Development of website](#Development)

   
* ### [Credits](#Credits)
 

 * [Authors](#Auth)
 * [Acknowledgements](#Acknow)



<a name="user"></a>
 ### User Experience (UX)

<a name="Pro"></a>
 * ### Project Goals

The project Goal is to create a backend developed database for a hardware store selecting the products of hardware supplied coupled with an Items page to provide which items and which date they are required for.
This would link into a website that woould show a gallery of photos for the products available and also a payment page that can be used once the customer is happy with there selection.

The Table used is of two categories one Item where you can select your items with a description and time stamp of when you require them. Also an urgent and product selection is added to this table function.
The other is products where a description of products is selected and you can edit or delete these products should you wish.
If you look at table.py it depicts the hardware db.




<a name="Dev"></a>
### Developer Business and Goals.


<img width="750" alt="main screenshot" src="https://live.staticflickr.com/65535/53298173743_d249dcc7ed_z.jpg">



<br><br>


The "Home. page", is a basic site that allows the use to choose items to add or categories to choose from.
The "add Items" page (as shown in the sceen shot above allows the use to select items fo purchasing.
The "products" page allows the customer to update and delete the categories as required.


<a name="User"></a>
### User Stories

As this is a backend developement site with a front end display it is more to allow the customer a selection of products that would be attached to a fully fuctional site to search and then purchase hardware from the supplier.
The customer builds up their selection of products then selects the items with the date for the supplier to deliver them.
The vendor can then add or delete the products if availabilty wasn't there but for it to function as a development project rather than functioning I've left the ability to edit and delete open for use.


<a name="Des"></a>
## Design

The design is based on the 'code institute' task manager backend developement learning page.

<a name="Font"></a>
### Font styles used

The font style is from materialize, this can be changed by adding "flow-text" to make it fit the sceen as suits.
The use of black text is simply functional.


<a name="Colour"></a>
### Colours and background images.

The colours are based on the Venezuelan flag. The background drop is the factory in connection that will supply the hardware.

<a name="Feat"></a>
### Features

The features are a home page showing the basic options, an Items selection page where the user can choose the items, then an item description allowing to put more information in. A due date for the items required. An urgent lever to select its an urgent purchase and a category selection to see if the product is available.

There is a product selection where in hind-site should only be allowed to be updated by the vendor but, due to real life issues and getting the database and python to function it has been left to function as dual entity which I appreciate is not viable if it was the finished article. This allows the choice of hardware to be selected via the products populated. if it was managed by staff they could delete a product if wasn't available or add once it became available.

<img width="750" alt="main screenshot" src="https://live.staticflickr.com/65535/53316691019_32c54bf266_b.jpg">

<a name="Deploy"></a>
### Deployment.

env.py file.

import os

os.environ.setdefault("IP", "0.0.0.0")
<br>
os.environ.setdefault("PORT", "5000")
<br>
os.environ.setdefault("SECRET_KEY", "any_secret_key")
<br>
os.environ.setdefault("DEBUG", "True")
<br>
os.environ.setdefault("DEVELOPMENT", "True")
<br>
os.environ.setdefault("DB_URL", "postgresql:///hardware")



This is saved as env.py as its blocked by Github so the page wont load unless this is added if you load with gitpod, code anywhere its fine.


To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 run.py.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt github deployment (did not use heroku Cli found going via github deployment option easier):

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. click view app on aceros-guayana (if not showing then follow steps below).
3. Open up the more selection button.
4. open run console
5. Type Python3
6. Then type "from hardware import db"
7. "db.create_all()
8. "exit()
9. Select open app

<img width="750" alt="main screenshot" src="https://live.staticflickr.com/65535/53310622191_667efca338_b.jpg">


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
* live.staticflickr.com
* cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css
* maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css
* Materialize
  
  

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
Using Html, CSS and Python.

* Glitch was used to format the code in Html  files.
* Checked via glitch for presentation.
  
<a name="w3-NU-HTML"></a>
* W3C was used to eliminate any glaring errors and conflicts on the web pages.
The WC3 did not like the use of any lines of code such as e.g. <script src="{{ url_for('static', filename='js/script.js') }}"></script>.
The use of curly braces kept thowing errors.
This is a python back end excercise so i've left the HTML pages as they were to link with the python pages.
I have put the HTML pages through Glitch to make them prettier for ease of eading the code.



<a name="Man-Test"></a>
### Manual Testing

If loading first time this may need to be used before acessing the web page.

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

When using Gitpod It needs time from the initial load to some of the Flask applictions as mentioned before the psycopg2 module seems very temperamental.

It does work in mobile screen format, but its a bit out of sync. 

<a name="development"></a>
### Development

As this is a backend project showing how to link database input information with a test of a front end image of a website. 
This can be developed into a fully fuctioning website linking it with a fully interactive payment page and a gallery showing images of the products/categories selected. The project is to show what a simple fuctioning database can do to aid a fucntioning web site or database led web page. With more refinement I can see how this would aid a fully fuctioning full stack web site. 

I would also have rather used photos of the different products than used a generic logo for the selections, but with time looming and not really wanting the base.html page to keep crashing I stuck with simplicity; for a future project it would look far more useful having visual aids for each selection.



<a name="Auth"></a>
### Authors

Code Institute-initial-work Alex Parry



<a name="Acknow"></a>
### Acknowledgments

*Code Institute:- base layout of website and code to create the pages.


*Robert Mclaughlin:- For reviewing ideas.



