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
    msg = db.Column(db.String(255), default='Hello, I am a student')
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
    msg = db.Column(db.String(255), default='Hello, I am a tutor')
    activation_token = db.Column(db.String(100), unique=True)
    registration_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Tutor {self.username}>'
    
class Subject(db.Model):
    __tablename__ = 'Subject'

    subjectId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subjectName = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Subject {self.subjectName}>'

class Student_Post(db.Model):
    __tablename__ = 'Student_Post'

    postId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    studentId = db.Column(db.Integer, db.ForeignKey('Student.studentId'), nullable=False)
    studentName = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    msg = db.Column(db.String(255), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    subjectId = db.Column(db.Integer, db.ForeignKey('Subject.subjectId'), nullable=False)
    subjectName = db.Column(db.String(50), nullable=False)
    available_time = db.Column(db.String(100), default='')
    status = db.Column(db.String(50), default='open', nullable=False)

    def __repr__(self):
        return f'<Student_Post {self.title}>'