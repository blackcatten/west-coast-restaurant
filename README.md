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
### Manual Testing:

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

3. Validator Python-pass

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

#### Testing on desktop:
- All steps are performed in browsers:
    - Chrome - Version 111.0.5563.65 
    - Microsoft Edge - Version 111.0.1661.44 
    - Firefox - 111.0

1. NAVIGATION BAR:

 - Hover over each link has been made. The effect has been confirmed to be correct.
 - The Home page link has been pressed and confirmed to take the user to the Home page.
 - The 'Make a Reservation' page link has been pressed and confirmed to take the user to the correctly page.
 - The 'Reservations detail' page link has been pressed and confirmed to take the user to the correctly page.
 - The Sign Up and Log in/ Log out page link has been pressed and confirmed to take the user to the responsive page.

2. FOOTER:

 - It has been verified that the footer is displayed as expected.

3. HOME PAGE:

 - It has been confirmed that the main image on the site is clear and shows up after the page loads.
 - All pictures on the home page have been reviewed and verified to be the correct size.
 - It has been confirmed that the title and text are correct and display correctly.

4. MAKE A RESRVATION PAGE:

 - It has been confirmed that if a user submits a form without filling out the required fields, a message is shown to complete them.
 - It has been confirmed that it shows a message with a valid date if the user enters a name other the date in the date input field.
 - it has been confirmed that after completing the form correctly and pressing submit, the user will go to the reservations detail page.

 5. RESERVATIONS DETAIL PAGE:

 - The data that was entered into the form on the Make a Reservation page has been transferred to and displayed in the booking details on the reservations detail page.

 6. LOGIN PAGE:

 - It has been confirmed that the main image on the site is clear and shows up after the page loads.

 - It has been confirmed that the title and text are correct and display correctly and on correctly place.
 - It has been confirmed that the online booking page form is laid out as expected.
 - It has been confirmed that if a user submits a form without filling out the required fields, a message is shown to complete them.
 - It has been confirmed that it shows a message with a valid username if the user enters a name other the username in the username input field.
 - It has been confirmed that it shows a message with a valid password if the user enters a name other the password in the password input field.
 - It has been confirmed that after completing the form correctly and pressing submit, the user will go to the home page.


7. SIGN UP PAGE:

 - It has been confirmed that the main image on the site is clear and shows up after the page loads.
 - It has been confirmed that the title and text are correct and display correctly and on correctly place.
 - It has been confirmed that the online booking page form is laid out as expected.
 - It has been confirmed that if a user submits a form without filling out the required fields, a message is shown to complete them.
 - It has been confirmed that it shows a message with a valid e-mail address if the user enters a name other the e-mail address in the e-mail input field.
 - Confirmed to display a message with the correct password if the user enters a different password than the first time, or if the password does not match the required arrangement.
 - It has been confirmed that after completing the form correctly and pressing submit, the user will go to the home page.

8. LOGOUT PAGE:

 - It has been confirmed that the title and text are correct and display correctly and on correctly place.
 - The button works properly, and after pressing log out button, the user is logged out.


9. UPDATE RESERVATION PAGE:

 - It has been confirmed that the main image on the site is clear and shows up after the page loads.
 - It has been confirmed that the title and text are correct and display correctly and on correctly place.
 - It has been confirmed that the update reservation page form is laid out as expected.
 - It has been confirmed that if a user submits a form without filling out the required fields, a message is shown to complete them.
 - It has been confirmed that it shows a message with a valid date if the user enters a name other the date in the date input field.
 - It has been confirmed that after completing the form correctly and pressing submit, the user will go to the reservations detail page.


10. DELETE RESERVATION PAGE:

 - It has been confirmed that the delete reservation message is correct and display correctly.

### All tests were also performed on:
- Samsung Galaxy s21
- Lenovo Tab M8(4th Gen)









## Known Bugs:

- Signup Page.


## Deployment:
## Deploying the app to Heroku:

Create a Heroku app.
To create a Heroku application, after log in, on the main page should press the button: 'New'. Then you should select: 'Create new app'. On the next page, you should fill a form with the following data: 'App name' and 'Choose a region', and then press button: 'Create app'.

Once the Heroku app is created, the next step is to go to option: 'settings'. In the category 'Config Vars', the user should press 'Reveal Config Vars' button, and then enter the KAY and VALUE for individual properties of:

- DATABASE_URL:

- SECRET_KEY

- CLOUDINARY_URL

- DISABLE_COLLECTSTATIC (Value of DISABLE_COLLECTSTATIC should be 1)

- PORT (Value of PORT should be 8000)

- Linking the repository to the app.
- Clicking on deploy branch. [My live project](https://west-coast-restaurant-901306ae347b.herokuapp.com/)

## Technologies Used:
### Languages Used:
### Frameworks, Libraries and Programs Used:
## Credits: 
### Content:
### Code:
### Media:
## Acknowledgements: