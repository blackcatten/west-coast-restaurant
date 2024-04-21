# West Coast Restaurant:
[My live project](https://west-coast-restaurant-901306ae347b.herokuapp.com/)

![responsive](media/responsive.png)

# Table of content:
## User Experience (UX):
### User Stories :
- as a user, it is easy to register on "sign up for free" and book a restaurant visit.
- as a user, it is easy to book a table after the user has registered and book a table on "make a reservation"
- as a user, it is easy to check which bookings have been made on "reservations detail".
- as a user it is easy to see the menu on the first page "homepage".
- as a user, it is easy to log in and log out using the "login/logout" button.
- as a user, you can see who made the page and see the address on the "footer".
- as a user, the wine list and desserts are also visible on the same page as the menu on the "home page" a little further down.
- as a user, it is easy to get to the homepage by clicking on "home" at the top left.
- as a user, the user are welcomed with the first thing that appears "Welcome to West Coast Restaurant
ALWAYS FRESH SEAFOOD"
- as a user, it is easy to edit your bookings and delete the booking.
- as a user, you can see the price of all items on the menus and can easily choose according to wallet if desired
- as an admin, I can easily confirm bookings via the admin page.
- as an admin, it is easy to see how many tables are available.

## Features:
### Existing Features:

1. Navigation bar.

- Navigation bar for desktop.

![nav desktop](media/nav_desktop.png)

![nav desktop login](media/nav_desktop_login.png)

- Navigation bar for ipad.

![nav ipad](media/nav_ipad.png)

- Navigation bar for iphone.

![nav iphone](media/nav_iphone.png)

2. Home Page.

![Homepage](media/homepage.jpeg)

3. Make a Reservation Page.

![Make_reservation](media/make_a_reservation.jpeg)

4. Reservations detail Page.

![Reservations_detail](media/reservations_detail.jpeg)

5. Login Page.

![login page](media/login.jpeg)

6. Logout Page.

![logout](media/logout.jpeg)

7. Signup Page.

![signup](media/signup.jpeg)

8. Alert Messages.

![alert messages](media/alert_message.png)

![alert messages warning](media/alert_messages_warning.jpeg)



## Typography:
## Design:
### Color:
### Wireframe:
![wireframe-home](media/wireframe-home-pp4.jpg)
![wireframe-makereservation](media/wireframe-makereservation-pp4.jpg)
![wireframe-reservations-detail](media/wireframe-reservations-detail-pp4.jpg)
![wireframe-signin](media/wireframe-siegnin-pp4.jpg)
![wireframe-signout](media/wireframe-signout-pp4.jpg)
![wireframe-signup](media/wireframe-signup-pp4.jpg)
## Testing:
### User Story Testing:
## Manual Testing:

1. Validator HTML-pass

- Homepage- pass 
![validator_homepage](media/validator_index.html_restaurant.jpeg)

- Make a Reservation Page- pass

![validator make a reservation](media/validator_make_reservation.html_restaurant.jpeg)

- Reservations Detail Page- pass

![validator reservations detail](media/validator_reservations_detail.html_restaurant.jpeg)

- Update reservations Page- pass

![validator update reservations](media/validator_update_reservation_restaurant.jpeg)

- Login Page- pass

![validator login](media/validator_login_restaurant.jpeg)

- Logout Page- pass

![validator logout](media/validator_logout_restaurant.jpeg)


2. Validator CSS-pass

![validator css](media/validator_css_restaurant.jpeg)

- admin.py booking_system- pass

![validator admin.py](media/validator_admin.jpeg)

- forms.py booking_system- pass

![validator forms.py](media/validator_forms.jpeg)

- models.py booking_system- pass

![validator models.py](media/valitator_models.jpeg)

- urls.py booking_system- pass

![validator urls.py](media/validator_urls_booking_system.jpeg)

- views.py booking_system- pass

![validator views.py](media/validator_pep8_restaurant.jpeg)

- settings.py west_coast- pass

![validator settings.py](media/validator_settings_west_coast.jpeg)

- urls.py west_coast- pass

![validator urls.py west_coast](media/validator_urls_west_coast.jpeg)

3. Validator Python-pass


## Known Bugs:

- Signup Page.


## Deployment:
## Deploying the app to Heroku:

Create a Heroku app.
To create a Heroku application, after log in, on the main page the user should press the button: 'New'. The user should select: 'Create new app'. On the next page, the user should fill a form with the following data: 'App name' and 'Choose a region', and then press button: 'Create app'.

Once the Heroku app is created, the next step is to go to option: 'settings'. In the category 'Config Vars', the user should press 'Reveal Config Vars' button, and then enter the KAY and VALUE for individual properties of:

DATABASE_URL:
To create DATABASE_URL, 

SECRET_KEY
To create a SECRET_KEY 

CLOUDINARY_URL
To create CLOUDINARY_URL,

DISABLE_COLLECTSTATIC
Value of DISABLE_COLLECTSTATIC should be 1

PORT Value of PORT should be 8000.

## Technologies Used:
### Languages Used:
### Frameworks, Libraries and Programs Used:
## Credits: 
### Content:
### Code:
### Media:
## Acknowledgements: