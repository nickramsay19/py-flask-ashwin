from flask import Flask

app = Flask(__name__) # Creates an instance of a flask app, with all the utilities prepared for us

# this defines a route, and what happens when we visit this route
@app.route('/') 
def hello_world():
    return 'Hello, World!'

'''
    How to run:
    Enter the following commands into terminal, while in the project directory
    export FLASK_ENV=development
    flask run

    This will start a local server
    On your browser visit "http://localhost:5000"

'''