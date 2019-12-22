# flask application configuration variable

import os
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG_GLOBAL = True

    # wep app port and name
    SERVER_NAME_WEB_APP = "/CashcogXCNT-Expenses/"
    PORT_WEB_APP = 5000

    # wep app port
    PORT_API_APP = 5001
    SERVER_NAME_API_APP = "/cashcogXCNT/api/v1"

    # Setup Database driver/ connect to DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'cashcog_expenses.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # stream urls
    CASHCOG_STREAM_URL = "https://cashcog.xcnt.io/stream"
    CASHCOG_SINGLE_URL = "https://cashcog.xcnt.io/single"

