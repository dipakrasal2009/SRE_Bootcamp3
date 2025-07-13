from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }
