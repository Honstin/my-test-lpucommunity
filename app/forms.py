from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    BooleanField,
    TextAreaField,
    FileField
    )
from wtforms.validators import (
    InputRequired, DataRequired,
    Email,Length, EqualTo, Required, ValidationError)
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug import secure_filename
from app.models import User

class UserForm(FlaskForm):
    username = StringField("username", [InputRequired(
        "Please enter your username.")])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Login')
    submit = SubmitField('Log In.')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField("Password", [Length(min=2),Required(),EqualTo(
        'confirm', message='Passwords must Match.')])
    confirm = PasswordField('Repeat password.')
    remember_me = BooleanField('Remember Login')
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(
        'Username Taken! Please choose another Username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
        'Email in use, please register a different e-mail.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    avatar = FileField('Update Profile Picture', validators=[FileAllowed(
        ['jpg', 'jpeg', 'png', 'gif'])])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(
            'You cannot choose the same name as someone else, pick another name'
            )