from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired

# Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

# Add Location Form
class AddLocationForm(FlaskForm):
    title = StringField('Location Title', validators=[DataRequired()])
    description = StringField('Location Description', validators=[DataRequired()])
    submit = SubmitField('Add')

# Add Sites Form
class AddSiteForm(FlaskForm):
    title = StringField('Site Title', validators=[DataRequired()])
    description = StringField('Site Description', validators=[DataRequired()])
    location = SelectField('Location', validators=[DataRequired()])
    submit = SubmitField('Add')
