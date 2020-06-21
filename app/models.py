from wtforms import Form, FloatField, validators

class InputForm(Form):
    lat = FloatField(
        label="Introduce la latitud del lugar", 
        validators=[validators.InputRequired()]
    )