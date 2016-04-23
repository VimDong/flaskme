#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
# manager = Manager(app)

# @app.route('/')
# def index():
#     return '<h1>Hello World</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello %s</h1>' % name

@app.route('/', methods=['GET', 'POST'])
def index():
        name = None
        form = NameForm()
        if form.validate_on_submit():
            session['name'] = form.name.data
            return redirect(url_for('index'))
        return render_template('index.html', form=form, name=session.get('name'))

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()
