from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Email,  ValidationError, EqualTo
import email_validator

class LoginForm(FlaskForm):
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

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    second_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

  
        
        