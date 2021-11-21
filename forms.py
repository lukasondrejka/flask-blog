from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, PasswordField, TextAreaField
from models import *


class BaseForm(FlaskForm):
    pass


class LoginForm(BaseForm):

    username = StringField(
        "Username",
        [DataRequired(), Length(min=3, max=30)]
    )

    password = PasswordField(
        "Password",
        [DataRequired(), Length(min=8)],
    )

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        user = User.where(username=self.username.data).first()
        if not user:
            self.username.errors.append('User not found')
            return False
        if not user.verify_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False
        return True


class CreateUserForm(BaseForm):

    username = StringField(
        "Username",
        [DataRequired(), Length(min=3, max=30)]
    )

    password = PasswordField(
        "Password",
        [DataRequired(), Length(min=8)],
    )

    def validate(self):
        initial_validation = super(CreateUserForm, self).validate()
        if not initial_validation:
            return False
        if User.where(username=self.username.data).first():
            self.username.errors.append('Username already exists')
            return False
        return True


class PostForm(BaseForm):

    title = StringField(
        "Title",
        [DataRequired()]
    )

    text = TextAreaField(
        "Text",
        [DataRequired()]
    )
