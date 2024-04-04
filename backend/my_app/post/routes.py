from flask import request, jsonify, render_template
import re
import uuid
from ..models import db, Student, Tutor, Subject, Student_Post
from flask import Blueprint
from datetime import date, datetime
import json

post = Blueprint("post", __name__)


@post.route("/create_post", methods=["POST"])
def create_post():
    username = request.form.get("username")
    title = request.form.get("title")
    post_date = datetime.now()
    msg = request.form.get("msg")
    salary = request.form.get("salary")
    subject_name = request.form.get("subject")
    available_time = request.form.get("available_time")
    timezone = request.form.get("timezone")
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
            timezone= "UTC " + timezone,
            status=status,
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created successfully"})


@post.route("/getAllOpeningPostsByUsername", methods=["GET"])
def getAllOpeningPostsByUsername():
    username = request.args.get("username")
    student = Student.query.filter_by(username=username).first()
    if student is None:
        return jsonify({"error": "Student not found"}), 401
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
                        "timezone": post.timezone,
                    }
                    for post in posts
                    if post.status == "opening"
                ]
            }
        )


@post.route("/getAllClosedPostsByUsername", methods=["GET"])
def getAllClosedPostsByUsername():
    username = request.args.get("username")
    student = Student.query.filter_by(username=username).first()
    if student is None:
        return jsonify({"error": "Student not found"}), 401
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
                        "timezone": post.timezone,
                    }
                    for post in posts
                    if post.status == "closed"
                ]
            }
        )


@post.route("/update_post", methods=["POST"])
def update_post():
    post_id = request.form.get("post_id")
    title = request.form.get("title")
    msg = request.form.get("msg")
    salary = request.form.get("salary")
    subject_name = request.form.get("subject")
    available_time = request.form.get("available_time")
    timezone = request.form.get("timezone")

    post = Student_Post.query.filter_by(post_id=post_id).first()
    if post is None:
        return jsonify({"error": "Post not found"})
    else:
        post.title = title
        post.post_date = datetime.now()
        post.msg = msg
        post.salary = salary
        post.subject_name = subject_name
        post.available_time = available_time
        post.timezone = timezone
        try:
            db.session.commit()
            return jsonify({"message": "Post updated successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500


@post.route("/inactivate_posts", methods=["POST"])
def inactivate_posts():
    post_id_list = json.loads(request.form.get("post_id_list"))
    for post_id in post_id_list:
        post = Student_Post.query.filter_by(post_id=post_id).first()
        post.status = "closed"
    try:
        db.session.commit()
        return jsonify({"message": "Posts inactivated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@post.route("/activate_post", methods=["POST"])
def activate_post():
    post_id = request.form.get("post_id")
    post = Student_Post.query.filter_by(post_id=post_id).first()
    post.status = "opening"
    post.post_date = datetime.now()
    try:
        db.session.commit()
        return jsonify({"message": "Posts activated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@post.route("/delete_posts", methods=["POST"])
def delete_posts():
    post_id_list = json.loads(request.form.get("post_id_list"))
    for post_id in post_id_list:
        post = Student_Post.query.filter_by(post_id=post_id).first()
        db.session.delete(post)
    try:
        db.session.commit()
        return jsonify({"message": "Posts deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


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


@post.route("/getPostByPostID", methods=["GET"])
def getPostByPostID():
    post_id = request.args.get("post_id")
    post = Student_Post.query.filter_by(post_id=post_id).first()
    if post is None:
        return jsonify({"error": "Post not found"}), 401
    else:
        return jsonify(
            {
                "post": {
                    "post_id": post.post_id,
                    "title": post.title,
                    "post_date": post.post_date,
                    "msg": post.msg,
                    "salary": post.salary,
                    "subject_name": post.subject_name,
                    "available_time": post.available_time,
                    "status": post.status,
                    "timezone": post.timezone,
                }
            }
        )


@post.route("/getAllOpeningPost", methods=["GET"])
def getAllOpeningPost():
    posts = Student_Post.query.all()
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
                    "timezone": post.timezone,
                }
                for post in posts
                if post.status == "opening"
            ]
        }
    )

@post.route("/GetUserNameByPostID", methods=["GET"])
def GetUserNameByPostID():
    post_id = request.args.get("post_id")
    post = Student_Post.query.filter_by(post_id=post_id).first()
    if post is None:
        return jsonify({"error": "Post not found"}), 401
    else:
        return jsonify({"username": post.username})