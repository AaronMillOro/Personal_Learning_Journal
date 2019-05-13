"""
Python Web Development Techdegree
Project 5 - Personal Journal Learning
--------------------------------
"""
from flask import (Flask, g, render_template, flash, redirect, url_for)

from peewee import *

#import models

DEBUG = True
PORT = 5000
HOST = '0.0.0.0'

app = Flask(__name__)


@app.route('/')
@app.route('/entries/')
def index():
    return render_template('index.html')


@app.route('/entries/new')
def new_entry():
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
