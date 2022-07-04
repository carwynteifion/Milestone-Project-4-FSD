#   [Bookable](https://milestone-project-4-fsd.herokuapp.com/)

Bookable is an online bookstore selling both fiction and non-fiction books in paperback and hardback formats at competitive prices. It offers deals, sales and clearance events. It also sells other products such as e-readers, as well as their world-renowned pink bookmarks!

---
 
## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Automated Testing**](#automated-testing)
    - [**Manual Testing**](#manual-testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

This is the final project in my Full-Stack Software Development course with [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/), in the **Full-Stack Frameworks** module.

### User Stories

As a user, I want to be able to:

- Create an account
- Log into the site
- Log out of the site
- Change password
- Have a profile page
- Fully edit my profile details
- View the site's products
- Have a shopping bag for me to add, remove, view or update quantities of products
- Check out securely
- View a summary of my order after purchase
- View my order history
- Write a review of a product
- Sign up to the site's mailing list

As a superuser, I want to be able to:

- Create, edit, update and delete product entries

### Design

The design of the site is based on standard Bootstrap elements, with some aspects altered using some custom CSS. The background image evokes an old library. Products and reviews are displayed as cards to maintain simplicity and readability.

#### Framework

Frameworks used in the project are:

- [Bootstrap 4](https://getbootstrap.com/)
    - Using the Bootstrap framework allowed for the development of a clean grid-based UI. Minimal effort was needed to edit any default classes.
- [Django 3.2](https://www.djangoproject.com/)
    - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - jQuery simplifies JavaScript to make scripting easier and faster in projects.

#### Colour Scheme

Rustic colours have been used to evoke an old library style. To ensure readability across the site, a white background has been maintained in content-heavy areas such as the products pages.

#### Typography

The primary fonts used on the site are those provided by the Bootstrap framework and the Google font [Lato](https://fonts.google.com/specimen/Lato).

### Wireframes

[Balsamiq Wireframes](https://balsamiq.com/) was used to create all of the wireframes during the design phase of this site. These can be found [here]().

##### back to [top](#table-of-contents)

---

## Features

All required feature as detailed in the brief have been implemented, as well as several additional features that offer greater overall user experience.
 
### Existing Features

**Status-dependant Navbar**

The options that a user will see displayed in the navbar are dependant on whether or not they are logged in.
- Users that are not logged in will see:
    - Bookable
    - Search
    - My Account (Register, Login)
    - Shopping Basket
- Users that are signed into the site will see:
    - Bookable
    - Search
    - My Account (Product Management (superusers only), My Profile, Logout)
    - Shopping Basket

Admins will be able to access the admin panel by adding '/admin' at the end of the site's home page URL.

**Create Account**

Users are able to create their own user account. The code checks against existing users in the database to ensure that the selected username is unique, and that both the username and password meet the minimum/maximum length requirements. Once registered the user is directed to the home page to begin browsing the site.

**User Profile Page**

Upon registering or logging into the site, users are able to navigate to their profile page. Here they can choose to edit their profile information, including delivery address.

**Logout**

Users that have logged into the site may end their session at any time by clicking the 'Logout' button on the navbar. Django ends their session and redirects the user to the homepage.

**Product Filtering**

Users are able to filter the displayed products based on their type by using the dropdown menus at the top of the page.

**Change password**

Users that have forgotten their password upon logging in can change their password following the Forgotten Password link. They can then log in using the updated password.

**Add to/View/Update/Remove from bag**

Users have full CRUD functionality over their own shopping bag. They can add products to the basket via the product details page, view the shopping bag from the bag icon on the navbar, and update the bag's contents using the quantity selector/update buttons or the remove button.

**Secure checkout**

Users can check out once they are happy with their order. They need a valid card number to process an order. Stripe ensures the checkout process is done securely. The checkout page auto-populates with a user's given profile information. An email is sent to the user upon a successful transaction.

**Sign up to newsletter**

Anyone can sign up to the newsletter by entering their email on the home page and agreeing to the site's privacy policy. They do not need to be logged in or have an account.

**Leave a review**

Logged-in users can leave a review on products providing they agree to the site's review guidelines, via the product's details page.

**Order Summary**

The order summary is shown once successfully checked out and payment processed. Users can opt to navigate to the Deals section of the site if they wish.

**Order History**

Order History can be viewed at the bottom of a user's profile page. Each link directs the user to an order's summary page.

### Features Left to Implement

I wanted to implement account deletion and further improve the site's UI/UX but ran out of time to do this before the deadline.

##### back to [top](#table-of-contents)

---

## Technologies Used

- [Microsoft Visual Studio Code](https://code.visualstudio.com/) - Open source IDE from Microsoft that was used to code this project.
- [GitHub](https://github.com/) - Remote repository for all project code with git version control.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - The fundamental code structure for all webpages.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - The fundamental stylesheet language for all webpages.
- [JavaScript ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - The scripting language for webpages.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Javascript framework used to implement custom code and initialize Materialize functions.
- [Bootstrap 4.4.1](https://getbootstrap.com/) - Primary visual model for this project.
- [Stripe](https://stripe.com/docs/api?lang=python) - The Stripe API allows individuals and businesses to make and receive payments over the Internet.

### Back-End Technologies

- **Heroku**
    - [Heroku](https://www.heroku.com) - Hosts the deployed version of this project.
    - [Heroku Postgres](https://www.heroku.com/postgres) - PostgreSQL is one of the world's most popular relational database management systems.
- **Python**
    - [Python 3.8.11](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language and is the language used for all backend functions of this project.
    - [Django 3.2.13](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Amazon Web Services**
    - [Amazon S3](https://aws.amazon.com/s3/) - Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface. Amazon S3 uses the same scalable storage infrastructure that Amazon.com uses to run its global e-commerce network.
    - [Amazon IAM](https://aws.amazon.com/iam) - Amazon Identity and Access Management (IAM) is a web service that helps securely control access to Amazon resources. IAM controls who is authenticated and authorised to use resources.

##### back to [top](#table-of-contents)

---

## Testing

Testing for this project has been completed using both automated and manual methods. 

### Automated Testing



### Manual Testing

Extensive manual testing has been completed to check that the site performs as it should in different environments and in different browsers.

An MS Excel workbook detailing these tests can be found [here](https://github.com/carwynteifion/milestone-project-4-fsd/blob/main/manual-testing/bookable_page_tests.xlsx).

### Validators

**HTML**

Passing the HTML from all templates and base into the [W3C Markup Validator](https://validator.w3.org/) generates no errors aside from Django templating issues which the validator does not recognise, and non-critical warnings regarding the `type` attribute not being required on `<script>` tags.

**CSS**

 Passing the project's CSS through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) shows that there are no errors.

**Javascript**

All Javascript was passes throught the [Esprima Syntax Validator](http://esprima.org/demo/validate.html) and was found to be syntactically valid.

**Python**

All Python code was passed through the [PEP8 Online](http://pep8online.com/) validator and is fully PEP8 compliant.

### Compatibility

The project was tested to ensure full usability across the following browsers and their mobile equivalents (where applicable):

- Chrome
- Firefox
- Edge (Chromium)

##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment

Before you are able to deploy and run this application locally, you must have the following installed on your system:

- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- An IDE of your choice, such as [Microsoft Visual Studio Code](https://code.visualstudio.com).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.

Next, perform the following steps:

Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    - `git clone https://github.com/carwynteifion/milestone-project-4-fsd.git`.
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file containing the following environmental variables:
    - ***STRIPE_PUBLIC_KEY*** - Used solely to identify your account with Stripe; it isn't secret.
    - ***STRIPE_SECRET_KEY*** -  Can perform any API request to Stripe without restriction.
    - ***SECRET_KEY*** - Standard secret key, any value.
    - ***STRIPE_WH_SECRET*** - Secret key used for Stripe webhooks.
    - ***AWS_ACCESS_KEY_ID*** - AWS user credentials.
    - ***AWS_SECRET_ACCESS_KEY*** - AWS S3 credentials.
    - ***EMAIL_HOST_USER*** - for sending emails through Gmail.
    - ***EMAIL_HOST_PASS*** - this should be a Gmail-generated app password, must enable 2FA first.
    - ***DATABASE_URL*** - Remote PostgreSQL database link if using a remote database.
    - ***USE_AWS*** - set to 'True' to use AWS on deployed site.

    You must create accounts with both Stripe and Amazon S3. Prior knowledge on how to configure a publicly accessible S3 Bucket and the Stripe API are assumed for this project, as detailed instructions are beyond the scope of this document.


- Install all requirements from the [requirements.txt](https://github.com/carwynteifion/Milestone-Project-4-FSD/blob/main/requirements.txt) file using this command:
    - `pip3 -r requirements.txt`

- At the terminal prompt, type ```python3 manage.py runserver```. Django should now start running a development server from 'http://127.0.0.1:8000'. Copy and paste this address to your browser.

    Running the project for the first time will cause Django to create a SQLite3 database named ```db.sqlite3```. Type the following command into the terminal to create the database schema:
    - `python3 manage.py migrate`

    Django will then migrate the files contained in the migrations folder to set up the following relational database schema:

    ![Relational Database Schema Diagram](media/readme_files/ms4_schema.png?raw=true "MS4 Schema")




### Remote Deployment

To implement this project on Heroku, the following must be completed:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/carwynteifion/Milestone-Project-4-FSD/blob/main/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `web: gunicorn bookable.wsgi:application`
    - My file can be found [here](https://github.com/carwynteifion/Milestone-Project-4-FSD/blob/main/bookable/wsgi.py).
3. Sign up for or log into your Heroku account, create your project app, and click the **Deploy** tab. Select *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as in the local deployment above.
5. In the **Resources** tab, go to the Add-ons section and add the Heroku Postgres add-on. Choose the *Hobby* level when prompted. This will give you a remote database to use for your project. The database URI will be located in the Config Vars in the **Settings** tab.
6. The app will now be deployed and built by Heroku and will be ready to run.
7. Alter your project's ```settings.py``` file to connect to the remote database using the ```dj_database_url``` Python package.
8. Follow the steps in the Local Deployments section above to migrate your schema to the remote database.

##### back to [top](#table-of-contents)

---

## Credits

### Content

- All product images and text, unless stated below, were adapted from their entries on [Amazon](https://amazon.co.uk/).
- CI's Boutique Ado project was used as a starting point, especially to implement Stripe, AWS etc.

### Media

- [Background image](https://unsplash.com/photos/YLSwjSy7stw/)
- [Bookmark](https://media.istockphoto.com/vectors/template-design-vector-for-paper-bookmarks-isolated-on-white-vector-id1311447327?b=1&k=20&m=1311447327&s=612x612&w=0&h=qHxHu23PJnL0YZD989hiZ17CP8xEjlFh8DC3s1L0fGA=/)
- [E-reader](https://thumbs.dreamstime.com/b/ereader-tablet-computer-28163143.jpg)
- [Default image](https://nnpdev.wustl.edu/img/BookCovers/genericBookCover.jpg)


### Acknowledgements

- My mentor, Chris, for being as supportive and as helpful as possible throughout this last year of coding!
- My fiancee, Isadora, her mum, Kay, and my fellow coder-in-crime Adam for extensively bug testing my site.

##### back to [top](#table-of-contents)