from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SubmitForm(FlaskForm):
    ''' Create a simple form for sending transactions '''
    amount = StringField('amount')
    submit = SubmitField('Send')
    receiver = StringField('receiver')

    
    
