from . import post

from flask import request, jsonify, render_template
import re
import uuid
from ..models import db, Student, Tutor, Subject, Student_Post

@post.route('/')
def home():
    return "This is the posting page"

@post.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    student = Student.query.filter_by(email=data['email']).first()
    subject = Subject.query.filter_by(subjectName=data['subject']).first()
    if student is None:
        return jsonify({'error': 'Student not found'})
    else:
        new_post = Student_Post(
            studentId=student.id,
            studentName=student.username,
            title=data['title'],
            date=data['date'],
            msg=data['msg'],
            salary=data['salary'],
            subjectId=subject.id,
            subjectName=subject.subjectName,
            available_time=data['available_time'],
            status='open'
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully'})
