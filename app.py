"""The expanse accounting webserver."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models import Base

app = Flask(__name__)
APPLICATION_NAME = "Expanse Accounting"
app.config["SECRET_KEY"] = "secret-key"

engine = create_engine("sqlite:///expense_accounting.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

from routes import *

if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(port=8080)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
