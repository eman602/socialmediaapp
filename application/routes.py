from flask import render_template, redirect, url_for, request
from application import app, bcrypt
from application import app, db
from application.models import Users
from application.forms import loginForm

@app.route('/', methods=['GET', 'POST'])
def login():
    form=loginForm()
    if form.validate_on_submit:
        login_email= Users.query.filter_by(email=form.email.data).first()
        login_password= Users.query.filter_by(email=form.password.data).first()
        if login_email and login_password:
            return render_template("welcome.html")


    return render_template("login.html", form=form)