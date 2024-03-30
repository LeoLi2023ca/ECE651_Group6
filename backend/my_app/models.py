from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "Student"

    username = db.Column(db.String(50), primary_key=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    grade = db.Column(
        db.Enum("kindergarten", "primary", "secondary", "bachelor", "graduate", "tbd"),
        default="tbd",
    )
    timezone = db.Column(db.VARCHAR(50), default="UTC")
    msg = db.Column(db.String(255), default="Hello, I am a student")
    # activation_token = db.Column(db.String(100), unique=True)
    # registration_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Student {self.username}>"


class Tutor(db.Model):
    __tablename__ = "Tutor"

    username = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    edu_level = db.Column(
        db.Enum("highschool", "bachelor", "master", "phd", "tbd"), default="tbd"
    )
    timezone = db.Column(db.VARCHAR(50), default="UTC")
    available_time = db.Column(db.String(100), default="")
    subject_name = db.Column(db.String(50), nullable=True)
    salary = db.Column(db.String(50), nullable=True)
    msg = db.Column(db.String(255), default="Hello, I am a tutor")
    # listed? Tutor setting to be listed(in student view of tutor list, same as status of student post) or not

    # activation_token = db.Column(db.String(100), unique=True)
    # registration_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Tutor {self.username}>"


class Subject(db.Model):
    __tablename__ = "Subject"
    subject_name = db.Column(db.String(50), primary_key=True, nullable=False)

    def __repr__(self):
        return f"<Subject {self.subject_name}>"


class Student_Post(db.Model):
    __tablename__ = "Student_Post"

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(
        db.String(50), db.ForeignKey("Student.username"), nullable=False
    )
    title = db.Column(db.String(50), nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    msg = db.Column(db.String(255), nullable=False)
    salary = db.Column(db.String(50), nullable=True)
    subject_name = db.Column(db.String(50), nullable=False)
    available_time = db.Column(db.String(100), default="")
    status = db.Column(db.String(50), default="open", nullable=False)

    def __repr__(self):
        return f"<Student_Post {self.title}>"


class ChatMessage(db.Model):
    __tablename__ = "ChatMessage"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_username = db.Column(db.String(50), nullable=False)
    receiver_username = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    parent_message_id = db.Column(
        db.Integer, db.ForeignKey("ChatMessage.id"), nullable=True
    )
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<ChatMessage {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "sender": self.sender_username,
            "receiver": self.receiver_username,
            "text": self.text,
            "parent_message_id": self.parent_message_id,
            "timestamp": self.timestamp,
        }
