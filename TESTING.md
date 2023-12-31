# Testing

Return back to the [README.md](README.md) file.

## Table of Contents
1. [Code Validation](#code-validation)
    1. [HTML](#html)
    2. [CSS](#CSS)
    2. [Python](#Python)
2. [Browser Compatibility](#browser-compatibility)
3. [Responsiveness](#responsiveness)
4. [Lighthouse Audit](#lighthouse-audit)
5. [Defensive Programming](#defensive-programming)
6. [User Story Testing](#user-story-testing)
7. [Automated Testing](#automated-testing)
    1. [Python](#python)
8. [Bugs](#bugs)


## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2F) | <details><summary>Home</summary>![screenshot](documentation/screenshots/html_home.jpg)</details> | Pass: No Errors |
| Bookings | [W3C Bookings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Fbookings_list%2F) | <details><summary>Booking</summary>![screenshot](documentation/screenshots/html_bookings_list.jpg) | Pass: No Errors |
| User Bookings | [W3C User Bookings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Fuser_bookings%2F) | <details><summary>User Bookings</summary>![screenshot](documentation/screenshots/html_user_bookings.jpg)</details> | Pass: No Errors |
| User Profile | [W3C User Profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Fuser_profile%2F) | <details><summary>User Profile</summary>![screenshot](documentation/screenshots/html_user_profile.jpg)</details> | Pass: No Errors |
| User Profile Update | [W3C User Profile Update](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Fuser_profile_update%2F) | <details><summary>User Profile Update</summary>![screenshot](documentation/screenshots/html_user_profile_update.jpg)</details> | Pass: No Errors |
| Sign Up | [W3C Sign Up](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Faccounts%2Fsignup%2F) | <details><summary>Sign Up</summary>![screenshot](documentation/screenshots/html_signup.jpg)</details> | Pass: No Errors |
| Sign In | [W3C Sign In](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Faccounts%2Flogin%2F) | <details><summary>Sign In</summary>![screenshot](documentation/screenshots/html_signin.jpg)</details> | Pass: No Errors |
| Sign Off | [W3C Sign Off](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Faccounts%2Flogout%2F) | <details><summary>Sign Off</summary>![screenshot](documentation/screenshots/html_signoff.jpg)</details> | Pass: No Errors |
| Posts Overview | [W3C Posts Overview](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Fposts_overview%2F) | <details><summary>Posts Overview</summary>![screenshot](documentation/screenshots/html_posts_overview.jpg)</details> | Pass: No Errors |
| Article | [W3C Article](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Fchoosing-the-best-dog-house%2F) | <details><summary>Article</summary>![screenshot](documentation/screenshots/html_article.jpg)</details> | Pass: No Errors |
| Contact | [W3C Contact](https://validator.w3.org/nu/?doc=https%3A%2F%2FCorentin-Vidick.github.io%2FP4-JSDogTraining%2Fcontact.html) | <details><summary>Contact</summary>![screenshot](documentation/screenshots/html_contact_us.jpg)</details> | Pass: No Errors |
| Contact Success | [W3C Contact Success](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjstraining.herokuapp.com%2Fcontact_success%2F) | <details><summary>Contact Success</summary>![screenshot](documentation/screenshots/html_contact_success.jpg)</details> | obsolete iframe warnings |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](documentation/screenshots/css_validation.jpg) | Pass: No Errors 

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| JSTraining | --- | --- | --- |
| settings.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/jstraining/settings.py) | <details><summary>Settings</summary>![screenshot](documentation/screenshots/pylinter/jstraining_settings.jpg)</details> | All clear, no errors found |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/jstraining/urls.py) | <details><summary>URLs</summary>![screenshot](documentation/screenshots/pylinter/jstraining_urls.jpg)</details> | All clear, no errors found |
| Blog | --- | --- | --- |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/blog/admin.py) | <details><summary>Admin</summary>![screenshot](documentation/screenshots/pylinter/blog_admin.jpg)</details> | All clear, no errors found |
| apps.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/blog/apps.py) | <details><summary>Apps</summary>![screenshot](documentation/screenshots/pylinter/blog_apps.jpg)</details> | All clear, no errors found |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/blog/models.py) | <details><summary>Models</summary>![screenshot](documentation/screenshots/pylinter/blog_models.jpg)</details> | All clear, no errors found |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/blog/urls.py) | <details><summary>URLs</summary>![screenshot](documentation/screenshots/pylinter/blog_urls.jpg)</details> | All clear, no errors found |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/blog/views.py) | <details><summary>Views</summary>![screenshot](documentation/screenshots/pylinter/blog_views.jpg)</details> | All clear, no errors found |
| Bookings | --- | --- | --- |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/bookings/admin.py) | <details><summary>Admin</summary>![screenshot](documentation/screenshots/pylinter/bookings_admin.jpg)</details> | All clear, no errors found |
| apps.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/bookings/apps.py) | <details><summary>Apps</summary>![screenshot](documentation/screenshots/pylinter/bookings_apps.jpg)</details> | All clear, no errors found |
| forms.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/bookings/forms.py) | <details><summary>Forms</summary>![screenshot](documentation/screenshots/pylinter/bookings_forms.jpg)</details> | All clear, no errors found |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/bookings/models.py) | <details><summary>Models</summary>![screenshot](documentation/screenshots/pylinter/bookings_models.jpg)</details> | All clear, no errors found |
| tests.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/bookings/tests.py) | <details><summary>Tests</summary>![screenshot](documentation/screenshots/pylinter/bookings_tests.jpg)</details> | All clear, no errors found |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/bookings/urls.py) | <details><summary>URLs</summary>![screenshot](documentation/screenshots/pylinter/bookings_urls.jpg)</details> | All clear, no errors found |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/bookings/views.py) | <details><summary>Views</summary>![screenshot](documentation/screenshots/pylinter/bookings_views.jpg)</details> | All clear, no errors found |
| Contact | --- | --- | --- |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/contact/admin.py) | <details><summary>Admin</summary>![screenshot](documentation/screenshots/pylinter/contact_admin.jpg)</details> | All clear, no errors found |
| apps.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/contact/apps.py) | <details><summary>Apps</summary>![screenshot](documentation/screenshots/pylinter/contact_apps.jpg)</details> | All clear, no errors found |
| forms.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/contact/forms.py) | <details><summary>Forms</summary>![screenshot](documentation/screenshots/pylinter/contact_forms.jpg)</details> | All clear, no errors found |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/contact/models.py) | <details><summary>Models</summary>![screenshot](documentation/screenshots/pylinter/contact_models.jpg)</details> | All clear, no errors found |
| tests.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/contact/tests.py) | <details><summary>Tests</summary>![screenshot](documentation/screenshots/pylinter/contact_tests.jpg)</details> | All clear, no errors found |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/contact/urls.py) | <details><summary>URLs</summary>![screenshot](documentation/screenshots/pylinter/contact_urls.jpg)</details> | All clear, no errors found |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/contact/views.py) | <details><summary>Views</summary>![screenshot](documentation/screenshots/pylinter/contact_views.jpg)</details> | All clear, no errors found |
| Home | --- | --- | --- |
| apps.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/home/apps.py) | <details><summary>Apps</summary>![screenshot](documentation/screenshots/pylinter/home_apps.jpg)</details> | All clear, no errors found |
| tests.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/home/tests.py) | <details><summary>Tests</summary>![screenshot](documentation/screenshots/pylinter/home_tests.jpg)</details> | All clear, no errors found |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/home/urls.py) | <details><summary>URLs</summary>![screenshot](documentation/screenshots/pylinter/home_urls.jpg)</details> | All clear, no errors found |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/home/views.py) | <details><summary>Views</summary>![screenshot](documentation/screenshots/pylinter/home_views.jpg)</details> | All clear, no errors found |
| User Profile | --- | --- | --- |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/user_profile/admin.py) | <details><summary>Admin</summary>![screenshot](documentation/screenshots/pylinter/userprofile_admin.jpg)</details> | All clear, no errors found |
| apps.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/user_profile/apps.py) | <details><summary>Apps</summary>![screenshot](documentation/screenshots/pylinter/userprofile_apps.jpg)</details> | All clear, no errors found |
| forms.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/user_profile/forms.py) | <details><summary>Forms</summary>![screenshot](documentation/screenshots/pylinter/userprofile_forms.jpg)</details> | All clear, no errors found |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/user_profile/models.py) | <details><summary>Models</summary>![screenshot](documentation/screenshots/pylinter/userprofile_models.jpg)</details> | All clear, no errors found |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/user_profile/urls.py) | <details><summary>URLs</summary>![screenshot](documentation/screenshots/pylinter/userprofile_urls.jpg)</details> | All clear, no errors found |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Corentin-Vidick/P4-JSDogTraining/main/user_profile/views.py) | <details><summary>Views</summary>![screenshot](documentation/screenshots/pylinter/userprofile_views.jpg)</details> | All clear, no errors found |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | <details><summary>Chrome</summary>![screenshot](documentation/screenshots/browser_chrome.jpg)</details> | Works as expected |
| Firefox | <details><summary>Firefox</summary>![screenshot](documentation/screenshots/browser_firefox.jpg)</details> | Works as expected |
| Edge | <details><summary>Edge</summary>![screenshot](documentation/screenshots/browser_edge.jpg)</details> | Works as expected |
| Brave | <details><summary>Brave</summary>![screenshot](documentation/screenshots/browser_brave.jpg)</details> | Works as expected |
| Opera | <details><summary>Opera</summary>![screenshot](documentation/screenshots/browser_opera.jpg)</details> | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile S (DevTools) | <details><summary>Mobile S</summary>![screenshot](documentation/screenshots/responsive/responsive_mobileS.jpg)</details> | Works as expected |
| Mobile IPhone 5 (DevTools) | <details><summary>Mobile IPhone 5</summary>![screenshot](documentation/screenshots/responsive/responsive_iphone5.jpg)</details> | Works as expected |
| Mobile IPhone 12 Pro (DevTools) | <details><summary>Mobile IPhone 12 Pro</summary>![screenshot](documentation/screenshots/responsive/responsive_iphone12pro.jpg)</details> | Works as expected |
| Mobile Galaxy S20 (DevTools) | <details><summary>Mobile Galaxy S20</summary>![screenshot](documentation/screenshots/responsive/responsive_galaxyS20.jpg)</details> | Works as expected |
| Tablet (DevTools) | <details><summary>Tablet</summary>![screenshot](documentation/screenshots/responsive/responsive_tablet.jpg)</details> | Works as expected |
| Laptop (DevTools) | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/responsive/responsive_laptop.jpg)</details> | Works as expected |
| Laptop L (DevTools) | <details><summary>Laptop L</summary>![screenshot](documentation/screenshots/responsive/responsive_L.jpg)</details> | Works as expected |
| 4K (DevTools) | <details><summary>4K</summary>![screenshot](documentation/screenshots/responsive/responsive_4k.jpg)</details> | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_home.jpg)</details> | All > 90 |
| Article | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_article.jpg)</details> | All > 90 |
| Bookings | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_bookings.jpg)</details> | Low performance |
| Contact Success | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_contactsuccess.jpg)</details> | All > 90 |
| Contact Us | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_contactus.jpg)</details> | All > 90 |
| Sig In | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_signin.jpg)</details> | All > 90 |
| Sign Off | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_signoff.jpg)</details> | All > 90 |
| Sign Up | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_signup.jpg)</details> | All > 90 |
| Stories | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_stories.jpg)</details> | All > 90 |
| User Bookings | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_userbookings.jpg)</details> | All > 90 |
| User Profile | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_userprofile.jpg)</details> | All > 90 |
| User Profile Update | Desktop | <details><summary>Laptop</summary>![screenshot](documentation/screenshots/lighthouse/lighthouse_userprofileupdate.jpg)</details> | Low performance |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Home | Redirection to Home page | Pass | |
| | Click on Navbar links | Redirection to appropriate page | Pass | |
| | Click on Footer links | Redirection to appropriate page | Pass | |
| Contact Page | | | | |
| | Click on Contact link in Footer | Redirection to Contact page | Pass | |
| | Enter email address | Field required | Pass | |
| | Enter message in textarea | Field will accept freeform text, field required | Pass | |
| | Click the Send button | Redirects user to confirmation page | Pass | |
| Sign Up | | | | |
| | Click on Sign Up link | Redirection to Sign Up page | Pass | |
| | Enter username | Field is required | Pass | |
| | Enter email address optional| Field is optional | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| Sign In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid username address | Field is required | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout link | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Bookings | | | | |
| | Click on Book Now button | User will be redirected to the Bookings page | Pass | |
| | Select session | Only available sessions are displayed | Pass | |
| | Fill in form | All fields mandatory except for Address Line 2 | Pass | |
| | Click on the Book Session button | User will be redirected to the booking confirmation page | Pass | |
| | Click on the Cancel button | User will be redirected to the home page | Pass | |
| My Account | | | | |
| | Click on My Account link | User will be redirected to the Profile page | Pass | |
| | Click on the Book Another Session button | User will be redirected to the booking page | Pass | |
| | Click on the Go To Booking Cancelation button | User will be redirected to the booking cancelation page | Pass | |
| | Click on the Create/Update Profile button | User will be redirected to the user profile update page | Pass | |
| | Click on the Delete Profile button | User will be prompted to confirm, then profile will be deleted | Pass | |
| Booking Cancelation | | | | |
| | Click on Go To Booking Cancelation button | User will be redirected to the booking cancelation page | Pass | |
| | Click on the Cancel Booking button | User will be prompted to confirm, then booking will be deleted | Pass | |
| Blog | | | | |
| | Click on Go To Stories link | User will be redirected to the story overview page | Pass | |
| | Click on a Story Image or Text | User will be redirected to the single post page | Pass | |
| Update Profile | | | | |
| | Click on Update Profile button | User will be redirected to the profile update page | Pass | |
| | Fill in the form | All fields mandatory except for Address Line 2 | Pass | |
| | Click on the Save button | User will be redirected to the my account page | Pass | |
| | Click on the Cancel button | User will be redirected to the my account page | Pass | |
| Delete Profile | | | | |
| | Click on Delete Profile button | User will be prompted to confirm, then profile will be deleted | Pass | |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user I can view the main page so that I can navigate through the website. | <details><summary>Home</summary>![screenshot](documentation/screenshots/home.jpg)</details> |
| As a user I can view the articles' overview so that see if I am interested in something. | <details><summary>Story</summary>![screenshot](documentation/screenshots/story.jpg)</details> |
| As a user I can contact the admin so that they can answer my question. | <details><summary>Contact</summary>![screenshot](documentation/screenshots/contact.jpg)</details> |
| As a user I can create an account so that I can log in and book a session / comment an article / create an account. | <details><summary>Sign Up</summary>![screenshot](documentation/screenshots/sign_up.jpg)</details> |
| As a site user I can be notified of my actions so that I can know my action was successful. | <details><summary>Alert</summary>![screenshot](documentation/screenshots/alert.jpg)</details> |
| As a site user I can view my bookings so that I can delete them if I want. | <details><summary>Cancel Booking</summary>![screenshot](documentation/screenshots/cancel_booking.jpg)</details> |
| As a site user I can delete a booking so that my session is cancelled. | <details><summary>Cancel Booking Alert</summary>![screenshot](documentation/screenshots/cancel_booking_alert.jpg)</details> |
| As a site user I can add a comment so that I can comment on an article. | <details><summary>Comment</summary>![screenshot](documentation/screenshots/comment.jpg)</details> |
| As a site user I can create/read/update/delete my profile so that update my personal details. | <details><summary>Profile Update</summary>![screenshot](documentation/screenshots/profile_create_update.jpg)</details> |
| As a site user I can log in/out so that access my account. | <details><summary>Sign In</summary>![screenshot](documentation/screenshots/sign_in.jpg)</details> |
| As a site user I can click on an available slot so that I can book a class. | <details><summary>Sessions</summary>![screenshot](documentation/screenshots/session.jpg)</details> |
| As a site administrator, I can view created profiles so that I can see users' information. | <details><summary>Admin Profiles</summary>![screenshot](documentation/screenshots/admin_profile.jpg)</details> |
| As a site administrator, I can view and delete booked sessions so that I can cancel a booking if I am too busy. | <details><summary>Admin Bookings</summary>![screenshot](documentation/screenshots/admin_bookings.jpg)</details> |
| As a site administrator, I can create/read/update/delete sessions so that I can manage my week's program. | <details><summary>Admin Sessions</summary>![screenshot](documentation/screenshots/admin_sessions.jpg)</details> |
| As a site administrator, I can view submitted contact forms so that I can answer their questions. | <details><summary>Admin contact</summary>![screenshot](documentation/screenshots/admin_contact.jpg)</details> |
| As a site administrator, I can create/read/update/delete articles for the Story page. | <details><summary>Admin stories</summary>![screenshot](documentation/screenshots/admin_story.jpg)</details> |
| As a site administrator, I can view/approve/delete comments to moderate the Thoughts section. | <details><summary>Admin Thoughts</summary>![screenshot](documentation/screenshots/admin_thoughts.jpg)</details> |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bookings | tests | 84% | ![screenshot](documentation/screenshots/test_bookings.jpg) |
| Contact | tests | 91% | ![screenshot](documentation/screenshots/test_contact.jpg) |
| Home | tests | 100% | ![screenshot](documentation/screenshots/test_home.jpg) |




## Bugs

### Issues

Booking form and Profile form cause low performance on Lighthouse due to Bootstrap CSS loading.

There are no remaining bugs that I am aware of.
