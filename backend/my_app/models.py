from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'Student'

    username = db.Column(db.String(50), primary_key=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    grade = db.Column(db.Enum('kindergarten', 'primary', 'secondary', 'bachelor', 'graduate', 'tbd'), default='tbd')
    timezone = db.Column(db.VARCHAR(50), default='UTC')
    msg = db.Column(db.String(255), default='Hello, I am a student')
    # activation_token = db.Column(db.String(100), unique=True)
    # registration_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Student {self.username}>'

class Tutor(db.Model):
    __tablename__ = 'Tutor'

    username = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    edu_level = db.Column(db.Enum('highschool', 'bachelor', 'master', 'phd'), default='tbd', nullable=False)
    timezone = db.Column(db.VARCHAR(50), default='UTC', nullable=False)
    available_time = db.Column(db.String(100), default='')
    msg = db.Column(db.String(255), default='Hello, I am a tutor')
    # activation_token = db.Column(db.String(100), unique=True)
    # registration_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Tutor {self.username}>'
    
class Subject(db.Model):
    __tablename__ = 'Subject'
    subject_name = db.Column(db.String(50), primary_key=True, nullable=False)

    def __repr__(self):
        return f'<Subject {self.subject_name}>'

class Student_Post(db.Model):
    __tablename__ = 'Student_Post'

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), db.ForeignKey('Student.username'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    msg = db.Column(db.String(255), nullable=False)
    salary = db.Column(db.String(50), nullable=True)
    subject_name = db.Column(db.String(50), nullable=False)
    available_time = db.Column(db.String(100), default='')
    status = db.Column(db.String(50), default='open', nullable=False)

    def __repr__(self):
        return f'<Student_Post {self.title}>'