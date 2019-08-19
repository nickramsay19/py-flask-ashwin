from flask import Flask

app = Flask(__name__) # Creates an instance of a flask app, with all the utilities prepared for us

# this defines a route, and what happens when we visit this route
@app.route('/') 
def hello_world():
    return 'Hello Ashwin! :)'

# this route allows for GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

'''
    How to run:

    1) Enter the pipenv shell/"container" & install required packages(flask)
    pipenv install
    pipenv shell
    
    2) Run the server
    export FLASK_APP=app
    export FLASK_ENV=development
    flask run

    This will start a local server
    On your browser visit "http://localhost:5000"

'''