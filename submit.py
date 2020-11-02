from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SubmitForm(FlaskForm):
    amount = StringField('amount')
    submit = SubmitField('Send')
    receiver = StringField('receiver')

    
    
