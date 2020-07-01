# Catcus Shop.

Catcus Shop is an eCommerce website dedicated to sell plants. This project is to support beginner, or advanced gardeners or what we know as “plant parents”, in a greeny-colourful journey. Gardening has proven to be beneficial for one's mood. In fact, gardening has even be prescribed in some situations where patients experience such things as anxiety and depression. 


## UX

My goal is to create a user-friendly, fully functional and appealing eCommerce. Before I started making this project I started watching several websites ideas, mainly from [Pinterest](https://www.pinterest.com/). Colours were chosen accordingly to the content used and the concept of colours in vegetation.

![Home section](https://github.com/elisamunoz/cactus-shop/blob/master/static/images/mockups/multi-device-mockup.jpg)

I used [Moqups](https://moqups.com/) to do the previous design of this project. [Here is the link for the mockups](https://github.com/elisamunoz/cactus-shop/tree/master/static/images/mockups).

### User Stories

#### “As a client I would like”:

- A website were I can shop plants to start my collection
- A website were I can shop plants to make my collection bigger and bigger
- A website were I can see trendy plants because I like to get what somebody else are getting 
- An online shop where I can get plants delivered in Ireland
- An online shop where I can get free shipping after buying a certain amount of money to save after buying plants
- An online shop were I can securely pay for my products and feel safe after paying online
- An online shop were apart from buying I also can learn something useful about the plants I am buying

#### “As a shop owner I need”#

- An appealing website to catch customers from the eye
- A website were I can upload products and update prices so I don't need to know any code
- A shop where the user can sign in, and sign up, so de users feel more secure about payment


### The sections of the website are:

### Home:
For this section I wanted to create a clean look, using light and bright colours. On this section I created a simple carousel to welcome the user to the shop.

#### About:
This subsection was made to show the user what to expect from the shop, such as delivery, contact and that it is possible to return products.

#### The Latest:
This section will show the latest 4 - 8 plants the shop owner uploads to the database.


## Technologies:

### Frontend
- HTML: as the skeleton of the project
- CSS: to give styles to the project
- Javascript: mainly to authenticate Stripe
- JQuery (3.2.1): to authenticate Stripe and add some features

### Libraries and external resources:
- Stripe (2.46): to realize payment
- Pillow (7.1): to be able to update images
- Bootstrap (4.3.1): to take components from this library
- Font Awesome (5.11.2): to get icons used in the project
- Google Fonts: to get fonts

### Backend 
- Django (1.11): To create the apps that make this website
- PostgreSQL: it is used for database

### Hosting
- Github: for version control of project code.
- S3 Buckets from AWS: to host images and static files including CSS and Javascript
- Heroku: to host the live view of this ptoject


## Features
- DOM creation
- User authentication
- Login required for certain tasks 
- Shopping cart creation and ability to update quantity of products wanted
- Credit/Debit card authentication to pay for products
- Error message when trying to get to a non-existent product or any invalid url
- "Your cart is currently empty" message when trying to open an empty shopping cart
- A default image is place when the shop owner uploads a product without an image
- Cart and checkout tables show free shipping when purchase is higher than €75
- Transparent to solid-fixed navbar
- Used CSS variables to set colors to make it easier to change color themes in the future if needed



## Feature I would like to implement:
- I created the url "/products/create" that can only be accessed by a super user, on this first version the super user can only create a new product using it. The super user can still upload, edit and delete products using the Django built-in admin panel. In a next version I would like to create the edit and delete functionality on the url.


## Testing
- Google Developer Tool: I used this tool to check every change I made on the code to check functionality and responsivenes in diferent device sizes
- [W3C Markup Validation Service](https://validator.w3.org/): I validated the HTML code using this validator. W3C Markup Validator does not recognize Django code as valid so I got errors pointing at them, 
- [CSS Validation Service](https://jigsaw.w3.org/css-validator/): I validated the CSS code using this validator.
- I used TestCase to test the Product app, to run it, it is necessary to run the following command in the terminal:
`$ python manage.py test`



## Deployment

This project was developed using Visual Studio IDE, I committed and pushed the code to GitHub to create an external version control repository to create back ups in case of unexpected major errors. This are the steps to deploy this project.

To see the code open the [Catcus Shop](https://elisamunoz.github.io/cactus-shop/) repository.

### Local Deployment:
To run the project locally. Install:
* Git
* Django

After installing these you need to:
1. Download this repository clicking in ‘Clone or Dowload’ on top of this page, then click on ‘Download ZIP’ and extract the files in the folder you will be working on.
2. Open the folder where you download the repository in your code editor
3. Create a `.env` file containing the following credentials:
`
os.environ["SECRET_KEY"] = "SECRET_KEY"
os.environ["STRIPE_PUBLISHABLE"] = "STRIPE_PUBLISHABLE"
os.environ["STRIPE_SECRET"] = "STRIPE_SECRET"
os.environ["DATABASE_URL"] = "DATABASE_URL"
os.environ["AWS_ACCESS_KEY_ID"] = "AWS_ACCESS_KEY_ID"
os.environ["AWS_SECRET_ACCESS_KEY"] = "AWS_SECRET_ACCESS_KEY"`

4. Install the required modules using this command:
`pip -r requirements.txt`

You can run the app by running: `python manage.py runserver`
The project will run at `http://127.0.0.1:8080`

### Remote Deployment
The application can be deploying using Heroku. Before, you need to:
* Create a requirements.txt file in the terminal, running the command `pip freeze > requirements.txt`
* Create a Procfile running the command `echo web: python app.py > Procfile`
* Commit and Push these files to the GitHub repository
* Create a new app at the Heroku dashboard.
* Link the app in Heroku to your GitHub respository
* Go to settings then to Reveal Config Vars and set to this:

KEY | VALUE 
---------- | ------------------------------------------------------------------------------------------------------------------
SECRET_KEY | `<your_secret_key>`
STRIPE_PUBLISHABLE | `<your_stripe_publishable_key>`
STRIPE_SECRET | `<your_stripe_secret_key>`
DATABASE_URL | `<your_database_url_key>`
AWS_ACCESS_KEY_ID | `<your_aws_access_key_id_key>`
AWS_SECRET_ACCESS_KEY | `<your_aws_seccret_access_key>`
DEBUG | FALSE

This credentials should match the key and values from your .env file

* Push your code to GithHub and Heroku
* Your app will be hosted at `http://<your_app_name>.herokuapp.com/`


## Credits
Features were taken and modified from these websites:

- Parallax effect: [Codepen Pen](https://codepen.io/corneliuslabuschagne/pen/rNaNgdB?editors=1000)
- Images were taken from [Pixabay](https://www.pixabay.com)
- Most of the text and plan images were taken from the online store [Gardens4You](https://www.gardens4you.ie/)
- Catcus logo taken from [Vecteezy](https://www.vecteezy.com/)
- I took inspiration from [Pinterest](https://www.pinterest.com)



