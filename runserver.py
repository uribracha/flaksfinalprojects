"""
This script runs the flaksfinalprojects application using a development server.
"""
import sys
from os import environ
from flaksfinalprojects import app
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.config['SECRET_KEY'] = 'aaaa'   
    app.run(HOST, PORT)
