from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    original_url = StringField('Вставьте ссылку',
                               validators=[DataRequired(message='Ссылка не может быть пустой'),
                                           URL(message='Неверная ссылка')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Получить короткую ссылку')
