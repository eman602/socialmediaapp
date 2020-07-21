from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Email,  ValidationError
import email_validator

class loginForm(FlaskForm):
    email = StringField('Email',
            validators=[
                    DataRequired(),
                    Email()
            ]
    
    )

    password = PasswordField('Password',
                validators = [
                    DataRequired()
                ]
    
    )

    remember= BooleanField('Remember Me')
    submit = SubmitField('Login')
