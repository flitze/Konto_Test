"""Initial expense accounting database population"""
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Account, Transaction

engine = create_engine('sqlite:///expense_accounting.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

account_payable = Account(name="payable")
account_receivable = Account(name="receivable")
account_cash_register = Account(name="cash_register")
account_rafael = Account(name="rafael")
account_mirjam = Account(name="mirjam")
account_mama = Account(name="mama")
account_manuela = Account(name="manuela")

session.add(account_manuela)
session.add(account_mama)
session.add(account_receivable)
session.add(account_mirjam)
session.add(account_rafael)
session.add(account_cash_register)
session.add(account_payable)
session.flush()
transaction_1 = Transaction(account_credit=account_mama.id,
                            account_debit=account_payable.id,
                            amount=15.16,
                            reason="Einkauf",
                            transaction_date=date.today())
session.add(transaction_1)

transaction_2 = Transaction(account_credit=account_cash_register.id,
                            account_debit=account_mama.id,
                            amount=15.16,
                            reason="Überweisung",
                            transaction_date=date.today())
session.add(transaction_2)

transaction_3 = Transaction(account_credit=account_mama.id,
                            account_debit=account_mama.id,
                            amount=15.16,
                            reason="Überweisung",
                            transaction_date=date.today())
session.add(transaction_3)

session.commit()
