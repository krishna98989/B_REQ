from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    age = IntegerField('Age', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Submit')

class BankForm(FlaskForm):
    bank_name = StringField('Bank Name', validators=[DataRequired(), Length(min=2, max=100)])
    account_number = StringField('Account Number', validators=[DataRequired(), Length(min=2, max=20)])
    ifsc_code = StringField('IFSC Code', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Submit')
