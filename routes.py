from datetime import datetime
from app import app, session
from flask import redirect, render_template, flash, url_for
from models import Account, Transaction
import forms


@app.route("/")
@app.route("/index")
def index():
    """
    Render Main Page
    :return:
    """
    transactions = session.query(Transaction).all()
    return render_template("index.html", transactions=transactions)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Add new transaction
    :return:
    """
    form = forms.AddTransactionForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        transaction = Transaction(account_credit=1, account_debit=2,
                                  amount=form.amount.data, reason=form.reason.data,
                                  transaction_date=datetime.utcnow())
        session.add(transaction)
        session.commit()
        flash("Transaction added to database")
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@app.route("/delete/<int:transaction_id>")
def delete(transaction_id):
    transaction = session.query(Transaction).get(transaction_id)
    if transaction:
        return render_template("delete.html", transaction=transaction)
    return redirect(url_for("index"))


@app.route("/edit")
def edit():
    return render_template("edit.html")
