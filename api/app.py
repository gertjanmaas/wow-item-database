import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_uri = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    os.environ.get('DB_USER', 'postgres'),
    os.environ.get('DB_PASS', 'postgres'),
    os.environ.get('DB_HOST', 'localhost'),
    int(os.environ.get('DB_PORT', 5432)),
    os.environ.get('DB_NAME', 'postgres')
    )

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from entities import Item