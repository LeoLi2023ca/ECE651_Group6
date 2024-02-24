from . import post

from flask import request, jsonify, render_template
import re
import uuid
from ..models import db, Student, Tutor, Subject, Student_Post

@post.route('/')
def home():
    return "This is the posting page"

@post.route('/createPost', methods=['POST'])
def createPost():
    data = request.get_json()
    student = Student.query.filter_by(username=data['username']).first()
    subject = Subject.query.filter_by(subjectName=data['subject']).first()
    if student is None:
        return jsonify({'error': 'Student not found'})
    else:
        new_post = Student_Post(
            studentId=student.studentId,
            studentName=student.username,
            title=data['title'],
            date=data['date'],
            msg=data['info'],
            salary=data['salary'],
            subjectId=subject.subjectId,
            subjectName=subject.subjectName,
            status='open'
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully'})
    
@post.route('/updatePost', methods=['POST'])
def updatePost():
    data = request.get_json()
    post = Student_Post.query.filter_by(id=data['postId']).first()
    if post is None:
        return jsonify({'error': 'Post not found'})
    else:
        post.title = data['title']
        post.date = data['date']
        post.msg = data['info']
        post.salary = data['salary']
        post.status = data['status']
        try:
            db.session.commit()
            return jsonify({'message': 'Post updated successfully'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        
@post.route('/deletePost', methods=['POST'])
def deletePost():
    data = request.get_json()
    post = Student_Post.query.filter_by(id=data['postId']).first()
    if post is None:
        return jsonify({'error': 'Post not found'})
    else:
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post deleted successfully'})
    
@post.route('/getAllPostsByStudentID', methods=['GET'])
def getAllPostsByStudentID():
    studentId = request.args.get('studentID')
    student = Student.query.filter_by(studentId=studentId).first()
    if student is None:
        return jsonify({'error': 'Student not found'})
    else:
        posts = Student_Post.query.filter_by(studentId=student.studentId).all()
        return jsonify([post.serialize() for post in posts])
    
@post.route('/getAllPostsBySubject', methods=['GET'])
def getAllPostsBySubject():
    subjectName = request.args.get('subject')
    subject = Subject.query.filter_by(subjectName=subjectName).first()
    if subject is None:
        return jsonify({'error': 'Subject not found'})
    else:
        posts = Student_Post.query.filter_by(subjectId=subject.subjectId).all()
        return jsonify([post.serialize() for post in posts])
    
@post.route('/getAllPostsByStatus', methods=['GET'])
def getAllPostsByStatus():
    status = request.args.get('status')
    posts = Student_Post.query.filter_by(status=status).all()
    return jsonify([post.serialize() for post in posts])

@post.route('/getPostByPostID', methods=['GET'])
def getPostByPostID():
    postId = request.args.get('postId')
    post = Student_Post.query.filter_by(postId=postId).first()
    if post is None:
        return jsonify({'error': 'Post not found'})
    else:
        return jsonify(post.serialize())