from flask_wtf import Form
from wtforms import SelectField, TextField, SubmitField


class ApiForm(Form):
    url = TextField("Enter URL")
    Extract = SelectField(
        'Extract',
        choices=[('lop', 'Links on a page'), ('lopd', 'Links on a Domain'), ('sp', 'Headers on a Single Page'), ('il',
                                                                                                                 'Headers Of First Children'), ('id',
                                                                                                                                                'Headers On a domain')]
    )
    submit = SubmitField("Submit")
