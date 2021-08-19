from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired


class AddTransactionForm(FlaskForm):
    """
    Form for transaction creation
    """
    amount = StringField("Amount", validators=[DataRequired()],
                         render_kw={"placeholder": "Amount"})
    reason = StringField("Reason", validators=[DataRequired()],
                         render_kw={"placeholder": "Reason"})
    submit = SubmitField("Submit")
