from wtforms import Form 
from wtforms import FloatField
from wtforms import validators

class InputForm(Form):
    lat = FloatField("Introduce la latitud del lugar", 
    [validators.Required()])