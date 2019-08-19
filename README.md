# Front end
Front end users HTML, CSS and Javascript

All the front end is, is a page or a collection of pages

You can add some level of functionality e.g. a game with javascript

# Back end
A back end is a program that runs on a computer and listens for HTTP requests.
The back end will SEND the correct front end, e.g. a login page when you REQEUST website.com/login

The back end can tell what page to send from the request:
    website.com/login
    will show a different page to:
    website.com/register

## Terminology
Domain name: website.com
IP Address: 124.171.25.86
Route: /home, /login, (/posts/<post-name> e.g. /posts/my-walk-to-the-park), /purchases/vape-juice/product-details

You dont need a domain name, but it is good for branding and memorability.

## Back end cont.
Backends essentially coordinate the website

### Functions of a server
* Serving the correct page for the correct ROUTE
* Handling users with login and register + security concerns with user passwords
* Utilising the database
* Logging requests somewhere, possibly logging any errors for debugging purposes
* Handling user sessions
    * Server might not let you visit certain pages unless you are logged in/have a valid session
    * Server might protect certain routes for administrators only
* Handling user input such as a web form(e.g. a login form, a search query, etc)