# Introduction to Servers and Web Developement
NOTE: This covers servers in general, not in python, we'll get to that later. If you understand this, flask will be easy to understand as long as you have a decent understanding of porgramming and python.

## The Front end
* Front end users HTML, CSS and Javascript
* All the front end is, is a page or a collection of pages
* You can add some level of functionality e.g. a game with javascript

## The Back end
* A back end is a program that runs on a computer and listens for HTTP requests. The back end will SEND the correct front end, e.g. a login page when you REQEUST `website.com/login`

* The back end can tell what page to send from the request:
    * `website.com/login` will show a different page to `website.com/register`

* Backends essentially coordinate the website

## Terminology
* Domain name: website.com
    * You dont need a domain name, but it is good for branding and memorability.
* IP Address: 124.171.25.86
* Route: /home, /login, (/posts/<post-name> e.g. /posts/my-walk-to-the-park), /purchases/vape-juice/product-details


#### Functions of a server
* Serving the correct page for the correct ROUTE
* Handling users with login and register + security concerns with user passwords
* Utilising the database
* Logging requests somewhere, possibly logging any errors for debugging purposes
* Handling user sessions
    * Server might not let you visit certain pages unless you are logged in/have a valid session
    * Server might protect certain routes for administrators only
* Handling user input such as a web form(e.g. a login form, a search query, etc)

## Advanced Topics
### HTTP
HTTP(Hyper Text Transfer Protocol) is a protocol for communication via the internet. It sets out a certain set of rules and formatting for requests. If you don't follow its rules, a server will not respond.


**HTTP Request**
* HTTP requests come in a few varieties.
    * GET
    * POST
    * HEAD
    * PUT
    * DELETE
    * CONNECT
    * OPTIONS
    * TRACE
    * PATCH

* For simplicity sake, you only need to know about GET and POST. A good acronym for most HTTP requests used in most web applications is CRUD:
    * Create --> Create a new instance of something - e.g. Registering an account - Usually refers to POST
    * Read --> To read or GET something - e.g. Viewing your facebook feed - Usually refers to GET
    * Update --> To update/edit an instance - e.g. Edit a facebook post of yours - Usually refers to PUT (sometimes PATCH)
    * Delete --> To delete an instance - e.g. delete a facebook post - Usually refers to... DELETE 
* CRUD is used because it makes sense in the context of a database, e.g. a database of facebook posts and users.

* Again, we only need to worry about GET and POST
    * We will use GET to GET a page e.g. GET website.com/posts --> sends the user a list of posts
    * We will use POST to POST information to the server e.g. POST username & password to login, website will handle the login with the information you provided and respond appropriately by logging you in or sending an error message("Username or password was incorrect.").

* For context, there are other protocols other than HTTP, they are all listed in the "TCP/IP Suite of protocols"
    * FTP (File Transfer Protocol) --> Uploading/downloading files, Used by Google Drive
    * SMTP (Simple Mail Transfer Protocol) --> used for emails
    * DHCP (Dynamic Host Configuration Protocol) --> Used when you first connect to wifi to give you a new IP assigned by the router
    * SSH (Secure Shell) --> Used for remotely connecting to a computer
    * And more. But, we only need to worry about HTTP.

**Sessions**
Excerpt from Flask documentation:
> In addition to the request object there is also a second object called session which allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically. What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.