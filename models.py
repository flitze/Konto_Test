from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """
    Create Account Table
    """
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)


class Transaction(Base):
    """
    Create Transaction Table
    """
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    account_credit = Column(Integer, ForeignKey('account.id'))
    account_debit = Column(Integer, ForeignKey('account.id'))
    amount = Column(Numeric(precision=2))
    reason = Column(String(250), nullable=False)
    transaction_date = Column(Date)


engine = create_engine('sqlite:///expense_accounting.db')
Base.metadata.create_all(engine)
