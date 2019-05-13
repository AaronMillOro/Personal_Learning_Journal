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


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
