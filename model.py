from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(100), nullable=False)

    # Relationship with Bank model
    bank = db.relationship('Bank', backref='student', uselist=False)

# Bank model
class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    bank_name = db.Column(db.String(100), nullable=False)
    account_number = db.Column(db.String(20), nullable=False)
    ifsc_code = db.Column(db.String(20), nullable=False)
