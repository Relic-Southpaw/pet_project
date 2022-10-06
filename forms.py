from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetForm(FlaskForm):
    name = StringField("Pet Name",  validators=[
                       InputRequired(message="Snack Name can't be blank")]) 
    species = SelectField("Species", choices = [('cat', 'cat'), ('dog','dog'),('porcupine', 'porcupine')])
    photo_url = StringField("Photo URL",  validators=[Optional(), URL()]) 
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message='Must be between 0 and 30')]) 
    notes = TextAreaField("Notes", validators=[Optional()]) 
    available = BooleanField("is available") 
