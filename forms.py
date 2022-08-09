# Creating forms is made easier by Flask
# flask_wtf -> flask wt forms
from flask_wtf import FlaskForm

# StringField -> simillar html input type text
# SubmitField -> simillar html input type submit
from wtforms import StringField, SubmitField

# use the validator 'DataRequired' to check whether field is filled or not
from wtforms.validators import DataRequired

# classes that extend flask form are used in every form created with flask form
class AddTaskForm(FlaskForm):
    title = StringField('Input Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class deleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')
    