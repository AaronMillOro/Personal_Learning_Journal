"""
Python Web Development Techdegree
Project 5 - Personal Journal Learning
--------------------------------
"""
from flask import (Flask, g, render_template, flash, redirect, url_for,
                   abort, request)

from peewee import *

import models
import forms

DEBUG = True
PORT = 5000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'passwordHARD2guess1234567890'


@app.before_request
def before_request():
    """Connect to DB before each request, using the 'g' variable"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the DB connection after each request."""
    g.db.close()
    return response


@app.route('/')
@app.route('/entries/')
def index():
    """Listing of all registered entries"""
    entries = models.Entry.select().order_by(models.Entry.date.desc()).limit(20)
    return render_template('index.html', entries = entries)


@app.route('/entries/new/', methods=['POST','GET'])
def new_entry():
    form = forms.EntryForm()
    if form.validate_on_submit():
        #validate_on_submit check if it's a POST request and if it's valid
        entry = models.Entry.create_entry(
            title= form.title.data,
            date = form.date.data,
            timespent = form.timespent.data,
            learned = form.learned.data,
            resources = form.resources.data
            )
        flash('Task successfully registered!')
        return redirect(url_for('index', entry_id = entry))
    return render_template('new.html', form=form)


@app.route('/entries/<entry_id>/', methods=['POST','GET'])
def entry_detail(entry_id):
    """Information items from an entry"""
    try:
        entry = models.Entry.get(models.Entry.id == entry_id)
    except IndexError:
        abort(404)
    except ValueError:
        abort(404)
    else:
        return render_template('detail.html', entry_id = entry)


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
