from flask import render_template, redirect, url_for, request
from application import app
from application.forms import loginForm

@app.route('/')
def login():
    form=loginForm()
    return render_template(login.html, title='Login Page', form=form)