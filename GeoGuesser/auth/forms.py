from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_wtf.file import FileRequired, FileAllowed

from ..models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    alias = StringField('Alias/Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists')
    
class LoginForm(FlaskForm):
    username = StringField('Alias/Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UploadGeoLocationForm(FlaskForm):
    image = FileField('Geo Location Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jfif'])])
    difficulty = StringField('Difficulty', validators=[DataRequired(), Length(min=4, max=20)])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Upload')