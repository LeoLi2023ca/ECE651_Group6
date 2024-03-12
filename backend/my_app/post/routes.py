from flask import request, jsonify, render_template
import re
import uuid
from ..models import db, Student, Tutor, Subject, Student_Post
from flask import Blueprint
from datetime import date

post = Blueprint("post", __name__)


@post.route("/create_post", methods=["POST"])
def create_post():
    username = request.form.get("username")
    title = request.form.get("title")
    post_date = date.today()
    msg = request.form.get("msg")
    salary = request.form.get("salary")
    subject_name = request.form.get("subject")
    available_time = request.form.get("available_time")
    status = "opening"

    student = Student.query.filter_by(username=username).first()
    # subject = Subject.query.filter_by(subjectName=subject_name).first()
    if student is None:
        return jsonify({"error": "Student not found"}), 401
    else:
        new_post = Student_Post(
            username=username,
            title=title,
            post_date=post_date,
            msg=msg,
            salary=salary,
            subject_name=subject_name,
            available_time=available_time,
            status=status,
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created successfully"})


@post.route("/getAllOpeningPostsByUsername", methods=["GET"])
def getAllPostsByUsername():
    username = request.args.get("username")
    student = Student.query.filter_by(username=username).first()
    if student is None:
        return jsonify({"error": "Student not found"})
    else:
        posts = Student_Post.query.filter_by(username=username).all()
        return jsonify(
            {
                "list": [
                    {
                        "post_id": post.post_id,
                        "title": post.title,
                        "post_date": post.post_date,
                        "msg": post.msg,
                        "salary": post.salary,
                        "subject_name": post.subject_name,
                        "available_time": post.available_time,
                        "status": post.status,
                    }
                    for post in posts
                    if post.status == "opening"
                ]
            }
        )


# @post.route('/updatePost', methods=['POST'])
# def updatePost():
#     data = request.get_json()
#     post = Student_Post.query.filter_by(id=data['postId']).first()
#     if post is None:
#         return jsonify({'error': 'Post not found'})
#     else:
#         post.title = data['title']
#         post.date = data['date']
#         post.msg = data['info']
#         post.salary = data['salary']
#         post.status = data['status']
#         try:
#             db.session.commit()
#             return jsonify({'message': 'Post updated successfully'})
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'error': str(e)}), 500

# @post.route('/deletePost', methods=['POST'])
# def deletePost():
#     data = request.get_json()
#     post = Student_Post.query.filter_by(id=data['postId']).first()
#     if post is None:
#         return jsonify({'error': 'Post not found'})
#     else:
#         db.session.delete(post)
#         db.session.commit()
#         return jsonify({'message': 'Post deleted successfully'})

# @post.route('/getAllPostsByStudentID', methods=['GET'])
# def getAllPostsByStudentID():
#     studentId = request.args.get('studentID')
#     student = Student.query.filter_by(studentId=studentId).first()
#     if student is None:
#         return jsonify({'error': 'Student not found'})
#     else:
#         posts = Student_Post.query.filter_by(studentId=student.studentId).all()
#         return jsonify([post.serialize() for post in posts])

# @post.route('/getAllPostsBySubject', methods=['GET'])
# def getAllPostsBySubject():
#     subjectName = request.args.get('subject')
#     subject = Subject.query.filter_by(subjectName=subjectName).first()
#     if subject is None:
#         return jsonify({'error': 'Subject not found'})
#     else:
#         posts = Student_Post.query.filter_by(subjectId=subject.subjectId).all()
#         return jsonify([post.serialize() for post in posts])

# @post.route('/getAllPostsByStatus', methods=['GET'])
# def getAllPostsByStatus():
#     status = request.args.get('status')
#     posts = Student_Post.query.filter_by(status=status).all()
#     return jsonify([post.serialize() for post in posts])

# @post.route('/getPostByPostID', methods=['GET'])
# def getPostByPostID():
#     postId = request.args.get('postId')
#     post = Student_Post.query.filter_by(postId=postId).first()
#     if post is None:
#         return jsonify({'error': 'Post not found'})
#     else:
#         return jsonify(post.serialize())
