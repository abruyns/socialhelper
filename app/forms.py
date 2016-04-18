from flask_wtf import Form
from wtforms import TextField, FileField, validators
 
class MessageForm(Form):

    phone_number = TextField('Recipient US Phone Number (ex: 2025551234)', 
        validators=[validators.Required(), validators.regexp(u'[0-9]+')])
    
    message_text = TextField('Message ')
    
    def validate(self):
        if not Form.validate(self):
            return False
        
        return True