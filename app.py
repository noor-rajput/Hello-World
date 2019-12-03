from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'
pp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
subs= db.Table('subs',
               db.column('student_id', db.Integer, db.ForeignKey('student.student_id')),
               db.column('subject_id', db.Integer, db.ForeignKey('subject.subject_id')))
class Students(db.Model):
   student_id = db.Column('student_id', db.Integer, primary_key = True)
   student_name = db.Column(db.String(100))
   student_city = db.Column(db.String(50))
   enrolled=db.relationship('Subjects', secondary=subs, backref=db.backref('enrolled', lazy='joined'))


   def __init__(self, student_name, student_city):
       self.student_name = student_name
       self.student_city = student_city

class Subjects(db.Model):
   subject_id = db.Column('student_id', db.Integer, primary_key = True)
   subject_name = db.Column(db.String(100))
   subject_code = db.Column(db.String(50))


   def __init__(self,  subject_name,subject_code):
       self.subject_name = subject_name
       self.subject_code = subject_code


