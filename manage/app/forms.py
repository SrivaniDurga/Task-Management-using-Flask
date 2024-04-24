# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    def __init__(self, users, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.users = users

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if username.data in self.users:
            raise ValidationError('Username already taken. Please choose a different one.')

class ForgotPasswordForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Reset Password')

# Define TaskForm here
class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    assign_to = StringField('Assign To', validators=[DataRequired()])
    priority = StringField('Priority', validators=[DataRequired()])
    duedate = DateField('Due Date', validators=[DataRequired()])
    submit = SubmitField('Create Task')
