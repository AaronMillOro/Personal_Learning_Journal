"""
Python Web Development Techdegree
Project 5 - Personal Journal Learning
--------------------------------
"""
from flask import (Flask, g, render_template, flash, redirect, url_for,
                   abort)

from peewee import *

import models
import forms

DEBUG = True
PORT = 5000
HOST = '0.0.0.0'

app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to DB before each request, using the 'g' variable"""
    g.db = models.DATABASE
    g.db.connect()
    #g.user = current_user


@app.after_request
def after_request(response):
    """Close the DB connection after each request."""
    g.db.close()
    return response


@app.route('/', methods=['POST','GET'])
@app.route('/entries/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/entries/new/', methods=['POST','GET'])
def new_entry():
    return render_template('new.html')


@app.route('/entries/<id>/', methods=['POST','GET'])
def entry_details():
    return render_template('detail.html')


@app.route('/entries/<id>/edit/', methods=['POST','GET'])
def edit_entry():
    return render_template('edit.html')


@app.route('/entries/<id>/delete/', methods=['POST','GET'])
def delete_entry():
    return render_template('index.html')


@app.errorhandler(404)
@app.errorhandler(TypeError)
def not_found(error):
    """Displays error message when a route does not exist"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
