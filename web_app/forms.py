from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField, StringField
from wtforms.validators import DataRequired, ValidationError


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    input_data = FileField('Test data', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_input_data(self, field):
        data = field.data
        if not data or not data.filename.endswith('.csv'):
            raise ValidationError('Only csv files allowed')
