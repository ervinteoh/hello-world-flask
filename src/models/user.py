import sqlalchemy as sa

from src.extensions import db


class User(db.Model):
    id = sa.Column(db.Integer, primary_key=True)
    firstname = sa.Column(db.String(100), nullable=False)
    lastname = sa.Column(db.String(100), nullable=False)
    email = sa.Column(db.String(80), unique=True, nullable=False)
    age = sa.Column(db.Integer)
    created_on = sa.Column(sa.DateTime, default=sa.func.now())
    updated_on = sa.Column(sa.DateTime, default=sa.func.now(), onupdate=sa.func.now())

    def __repr__(self):
        return f"<User {self.firstname}>"
