from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length

class SionForm(FlaskForm):
    nim = StringField('Nim',validators=[DataRequired(),Length(min=3,max=10)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=3)])
    harapan = RadioField("Harapan untuk semua matkul ?",choices=[('1','1'),('1','-1')],validators=[DataRequired()])
    submit = SubmitField('Submit')
