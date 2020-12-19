from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField, StringField, SelectField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import TextArea


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    content = StringField('Content', widget=TextArea(), validators=[DataRequired()])
    author = SelectField('Author', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    input_data = FileField('Test data', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_input_data(self, field):
        data = field.data
        if not data or not data.filename.endswith('.csv'):
            raise ValidationError('Only csv files allowed')
