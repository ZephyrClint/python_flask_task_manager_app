# import db instance from app module(app.py)
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id will be updated automatically
    title = db.Column(db.String(100), nullable=False) # title should be of maximum size 100 and cannot be null
    date = db.Column(db.Date, nullable=False)

    # definition of function which will represent each instance of the data model
    def __repr__(self):
        # dot format can be used instead of f string
        return f'{self.title} created on {self.date}'