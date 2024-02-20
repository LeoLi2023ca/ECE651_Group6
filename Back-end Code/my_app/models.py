from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'Student'

    studentId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    grade = db.Column(db.Enum('kindergarten', 'primary', 'secondary', 'bachelor', 'graduate', 'tbd'), default='tbd', nullable=False)
    timezone = db.Column(db.VARCHAR(50), default='UTC', nullable=False)
    msg = db.Column(db.String(100), default='Hello, I am a student')
    activation_token = db.Column(db.String(100), unique=True)
    registration_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Student {self.username}>'

class Tutor(db.Model):
    __tablename__ = 'Tutor'

    tutorId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    eduBackground = db.Column(db.Enum('highschool', 'bachelor', 'master', 'phd'), default='tbd', nullable=False)
    timezone = db.Column(db.VARCHAR(50), default='UTC', nullable=False)
    availableTime = db.Column(db.String(100), default='')
    msg = db.Column(db.String(100), default='Hello, I am a tutor')
    activation_token = db.Column(db.String(100), unique=True)
    registration_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Tutor {self.username}>'
