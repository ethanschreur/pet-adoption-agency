from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    """Wtform for creating a new pet"""
    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['Cat', 'Dog', 'Porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """creates wtform for editing a pet that is already created"""
    photo_url = StringField("Photo URL")
    notes = StringField("Notes")
    available = BooleanField("Available")