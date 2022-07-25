from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instance of flask
app = Flask(__name__)

# ideally, the secret key (for csrf_token) should be accessed as an environment variable
app.config['SECRET_KEY'] = 'sskl-key-csrf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# db stores the db object returned from SQLAlchemy method
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)