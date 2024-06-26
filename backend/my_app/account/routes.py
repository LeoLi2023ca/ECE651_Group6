from flask import request, jsonify, render_template
from werkzeug.security import generate_password_hash
from flask_mail import Message, Mail
import re
import uuid
from ..models import db, Student, Tutor

# from my_app import mail, mysql
from flask import Blueprint

account = Blueprint("account", __name__)
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# mail = current_app.extensions['mail']
# mysql = current_app.extensions['mysql']
mail = Mail()

@account.route("/validate_username", methods=["POST"])
def validate_username():
    username = request.form.get("username")

    existing_student = Student.query.filter(
        (Student.username == username)
    ).first()
    existing_tutor = Tutor.query.filter(
        (Tutor.username == username)
    ).first()

    return (
        jsonify(
            {
                "message": "ok",
                "isValid": not (existing_student or existing_tutor),
            }
        ),
        201,
    )

@account.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form.get("email")
    if not re.match(email_regex, email):
        return (
            jsonify(
                {
                    "message": "Email Format is Wrong!",
                    "isValid": False,
                    "FormatError": True
                },
                201
            )
        )

    existing_student = Student.query.filter(
        (Student.email == email)
    ).first()
    existing_tutor = Tutor.query.filter(
        (Tutor.email == email)
    ).first()

    return (
        jsonify(
            {
                "message": "ok",
                "isValid": not (existing_student or existing_tutor),
                "FormatError": False
            }
        ),
        201,
    )

@account.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    role = request.form.get("role")  # 'Student' or 'Tutor'
    # hashed_password = generate_password_hash(password)
    token = str(uuid.uuid4())  # Generate a unique activation token

    # Validate email format
    if not re.match(email_regex, email):
        return jsonify({"isSuccess": True, "error": "Invalid email format"}), 400

    # Check for duplicate username or email
    existing_student = Student.query.filter(
        (Student.username == username) | (Student.email == email)
    ).first()
    existing_tutor = Tutor.query.filter(
        (Tutor.username == username) | (Tutor.email == email)
    ).first() 
    if existing_student or existing_tutor:
        return jsonify({"isSuccess": True, "error": "Username or email already exists."}), 409

    # Add new student to the session and commit
    try:
        user_info = None
        code = None
        if role == "Student":
            user = Student(
                username=username,
                nickname=username,
                password=password,
                email=email,
                activation_token=token
            )
            user_info = {
                "username": user.username,
                "nickname": user.password,
                "email": user.email,
                "grade": user.grade,
                "timezone": user.timezone,
                "msg": user.msg,
            }
            code = "1"
            db.session.add(user)
            send_welcome_mail(email, token)
            db.session.commit()
        elif role == "Tutor":
            user = Tutor(
                username=username,
                nickname=username,
                password=password,
                email=email,
                activation_token=token
            )
            user_info = {
                "username": user.username,
                "nickname": user.password,
                "email": user.email,
                "edu_level": user.edu_level,
                "timezone": user.timezone,
                "available_time": user.available_time,
                "msg": user.msg,
            }
            code = "2"
            db.session.add(user)
            send_welcome_mail(email, token)
            db.session.commit()

        return (
            jsonify(
                {
                    "message": "Account added successfully!",
                    "code": code,
                    "user_info": user_info,
                    "isSuccess": True
                }
            ),
            201,
        )
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 502

@account.route('/getActivationToken', methods=["GET"])
def getActivationToken():
    username = request.args.get('username')
    existing_student = Student.query.filter(
        (Student.username == username)
    ).first()
    existing_tutor = Tutor.query.filter(
        (Tutor.username == username)
    ).first()
    token = ""
    if existing_student:
        token = existing_student.activation_token
    else:
        token = existing_tutor.activation_token
    return jsonify({'token': token}), 200

@account.route('/activate')
def activate():
    token = request.args.get('token')
    if not token:
        return "Activation token is missing", 400

    # Query the database for the token
    student_user = Student.query.filter_by(activation_token=token).first()
    tutor_user = Tutor.query.filter_by(activation_token=token).first()

    if student_user:
        # Token is valid, activate the account and remove the token
        # return jsonify({'error': 'fuck'}), 210
        student_user.registration_completed = True
        student_user.activation_token = None
        try:
            db.session.commit()
            return render_template('activation_success.html')
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    elif tutor_user:
        # Token is valid, activate the account and remove the token
        tutor_user.registration_completed = True
        tutor_user.activation_token = None
        try:
            db.session.commit()
            return render_template('activation_success.html')
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return "Invalid or expired activation link.", 401


@account.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    # print(username, password)
    existing_student = Student.query.filter((Student.username == username)).first()
    existing_tutor = Tutor.query.filter((Tutor.username == username)).first()
    user = existing_student if existing_student else existing_tutor


    # Check if the user exists and the password is correct
    # if user and user.password == password:
    #     if user.registration_completed==1:
    #         return jsonify({'message': 'Login successful!'})
    #     else:
    #         return jsonify({'error': 'Account is not activated.'}), 401
    # else:
    #     return jsonify({'error': 'Invalid email or password'}), 401
    if not existing_student and not existing_tutor:
        return jsonify({"error": "User not found"}), 404
    user_info = (
        {
            "username": user.username,
            "nickname": user.password,
            "email": user.email,
            "grade": user.grade,
            "timezone": user.timezone,
            "msg": user.msg,
        }
        if existing_student
        else {
            "username": user.username,
            "nickname": user.password,
            "email": user.email,
            "edu_level": user.edu_level,
            "timezone": user.timezone,
            "available_time": user.available_time,
            "msg": user.msg,
            "subjects": user.get_subjects(),
            "salary": user.salary,
        }
    )
    code = "1" if existing_student else "2"
    if user and user.password == password:
        if user.registration_completed:
            if code == "2" and not user.welcome_form_completed:
                return jsonify(
                    {"message": "Login successful!", "code": code, "user_info": user_info, "to_welcome_form": True}
                )
            else:
                return jsonify(
                    {"message": "Login successful!", "code": code, "user_info": user_info, "to_welcome_form": False}
                )
        else:
            return jsonify({"error": "Your account is not yet activated.", "code": "0"}), 401
    else:
        return jsonify({"error": "Invalid username or password.", "code": "0"}), 401


@account.route("/getStudentProfileByUsername", methods=["get"])
def getStudentProfileByUsername():
    username = request.form.get("username")
    user = Student.query.filter((Student.username == username)).first()
    if user:
        user_info = {
            "username": user.username,
            "nickname": user.password,
            "email": user.email,
            "grade": user.grade,
            "timezone": user.timezone,
            "msg": user.msg,
        }
        return jsonify({"message": "Get profile", "user_info": user_info})
    else:
        return jsonify({"error": "User not found", "code": "0"}), 401


@account.route("/getTutorProfileByUsername", methods=["get"])
def getTutorProfileByUsername():
    username = request.args.get("username")
    tutor = Tutor.query.filter((Tutor.username == username)).first()
    if tutor:
        user_info = {
            "username": tutor.username,
            "nickname": tutor.nickname,
            "edu_level": tutor.edu_level,
            "subjects": tutor.get_subjects(),
            "msg": tutor.msg,
            "salary": tutor.salary,
            "timezone": tutor.timezone,
            "available_time": tutor.available_time,
        }
        return jsonify({"message": "Get profile", "user_info": user_info})
    else:
        return jsonify({"error": "User not found", "code": "0"}), 401


@account.route("/updateStudentProfile", methods=["post"])
def updateStudentProfile():
    username = request.form.get("username")
    nickname = request.form.get("nickname")
    email = request.form.get("email")
    grade = request.form.get("grade")
    timezone = request.form.get("timezone")
    message = request.form.get("message")
    user = Student.query.filter((Student.username == username)).first()
    if user:
        user.nickname = nickname
        user.email = email
        user.grade = grade
        user.timezone = timezone
        user.msg = message
        db.session.commit()
        user_info = {
            "username": username,
            "nickname": nickname,
            "email": email,
            "grade": grade,
            "timezone": timezone,
            "msg": message,
        }
        return jsonify({"message": "profile updated", "user_info": user_info})
    else:
        return jsonify({"error": "User not found", "code": "0"}), 401


@account.route("/updateTutorProfile", methods=["post"])
def updateTutorProfile():
    username = request.form.get("username")
    nickname = request.form.get("nickname")
    email = request.form.get("email")
    edu_level = request.form.get("edu_level")
    timezone = request.form.get("timezone")
    available_time = request.form.get("available_time")
    message = request.form.get("message")
    subjects = request.form.get("subjects")
    school_name = request.form.get("school_name")
    subjects = subjects.split(",")
    salary = request.form.get("salary")
    # print(subjects)
    user = Tutor.query.filter((Tutor.username == username)).first()
    if user:
        user.nickname = nickname
        user.email = email
        user.school_name = school_name
        user.edu_level = edu_level
        user.timezone = timezone
        user.available_time = available_time
        user.msg = message
        user.set_subjects(subjects)
        user.salary = salary
        user.welcome_form_completed = True
        db.session.commit()
        user_info = {
            "username": username,
            "nickname": nickname,
            "email": email,
            "school_name": school_name,
            "edu_level": edu_level,
            "timezone": timezone,
            "available_time": available_time,
            "msg": message,
            "subjects": user.get_subjects(),
            "salary": salary,
        }
        return jsonify({"message": "profile updated", "user_info": user_info})
    else:
        return jsonify({"error": "User not found", "code": "0"}), 401


# @account.route('/forgetPwd', methods=['POST'])
# def forget_password():
#     email = request.json['email']
#     existing_student = Student.query.filter((Student.email == email)).first()
#     existing_tutor = Tutor.query.filter((Tutor.email == email)).first()
#     user = existing_student if existing_student else existing_tutor

#     if user:
#         try:
#             token = str(uuid.uuid4())  # Generate a unique activation token
#             user.activation_token = token
#             send_forget_pwd_mail(email, token)
#             db.session.commit()
#             return jsonify({'message': 'Reset password email has been sent!'})
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'error': str(e)}), 500
#     else:
#         return jsonify({'error': 'User not found'}), 404

# @account.route('/resetPwd')
# def reset_password():
#     token = request.args.get('token')
#     if not token:
#         return "Reset token is missing", 400

#     # Query the database for the token
#     student_user = Student.query.filter_by(activation_token=token).first()
#     tutor_user = Tutor.query.filter_by(activation_token=token).first()

#     if student_user:
#         # Token is valid, remove the token
#         student_user.activation_token = None
#         try:
#             db.session.commit()
#             return render_template('reset_password.html')
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'error': str(e)}), 500
#     elif tutor_user:
#         # Token is valid, remove the token
#         tutor_user.activation_token = None
#         try:
#             db.session.commit()
#             return render_template('reset_password.html')
#         except Exception as e:
#             db.session.rollback()
#             return jsonify({'error': str(e)}), 500
#     else:
#         return "Invalid or expired reset link."


@account.route("/updatePassword", methods=["POST"])
def update_password():
    username = request.form.get("username")
    password = request.form.get("old_pass")
    new_password = request.form.get("new_pass")
    existing_student = Student.query.filter((Student.username == username)).first()
    existing_tutor = Tutor.query.filter((Tutor.username == username)).first()
    user = existing_student if existing_student else existing_tutor

    if user:
        if password == user.password:
            user.password = new_password
            try:
                db.session.commit()
                return jsonify({"message": "Password updated successfully!"})
            except Exception as e:
                db.session.rollback()
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "Incorrect Old Password"}), 411

    else:
        return jsonify({"error": "User not found"}), 404

@account.route('/getStudentInfoByUsername', methods=['GET']) # pragma: no cover
def get_student_info_by_id():
    username = request.args.get('username')
    student = Student.query.filter_by(id=username).first()
    if student:
        return jsonify({'username': student.username, 'email': student.email, 'grade': student.grade, 'timezone': student.timezone, 'msg': student.msg})
    else:
        return jsonify({'error': 'Student not found'}), 404

def activation_token(): # pragma: no cover
    return str(uuid.uuid4())

def send_welcome_mail(email, token):
    activation_url = 'http://127.0.0.1:5000/activate?token={}'.format(token)
    html_content = render_template('activation_email.html', activation_url=activation_url)
    msg = Message('Welcome to OnlineTutor', sender = 'peter@mailtrap.io', recipients=[email], html=html_content)
    # msg.body = 'Welcome to OnlineTutor! Please click the link below to activate your account:\nhttp://127.0.0.1:5000/activate?token={}'.format(token)
    with account.open_resource('../static/OnlineTutor.jpg') as fp:
        msg.attach('logo.png', 'image/png', fp.read(), 'inline', headers=[['Content-ID', '<OnlineTutorLogo>']])
    mail.send(msg)

def send_forget_pwd_mail(email, token): # pragma: no cover
    reset_url = 'http://127.0.0.1:5000/resetPwd?token={}'.format(token)
    html_content = render_template('forget_pwd_email.html', reset_url=reset_url)
    msg = Message('OnlineTutor reset password', recipients=[email], html=html_content)
    # msg.body = 'Welcome to OnlineTutor! Please click the link below to activate your account:\nhttp://127.0.0.1:5000/activate?token={}'.format(token)
    with account.open_resource('../static/OnlineTutor.jpg') as fp:
        msg.attach('logo.png', 'image/png', fp.read(), 'inline', headers=[['Content-ID', '<OnlineTutorLogo>']])
    mail.send(msg)


@account.route("/getAllTutor", methods=["GET"])
def getAllTutor():
    tutors = Tutor.query.all()
    return jsonify(
        {
            "list": [
                {
                    "username": tutor.username,
                    "nickname": tutor.nickname,
                    "edu_level": tutor.edu_level,
                    "subjects": tutor.get_subjects(),
                    "school_name": tutor.school_name,
                    "msg": tutor.msg,
                    "salary": tutor.salary,
                    "timezone": tutor.timezone,
                    "available_time": tutor.available_time,
                }
                for tutor in tutors
                # if tutor.listed == "opening"
            ]
        }
    )

@account.route("/studentRequestMatching", methods=["POST"])
def studentRequestMatching():
    student_username = request.args.get("student_username")
    tutor_username = request.args.get("tutor_username")
    student = Student.query.filter((Student.username == student_username)).first()
    tutor = Tutor.query.filter((Tutor.username == tutor_username)).first()
    if student and tutor:
        student.tutors_asked.append(tutor_username)
        tutor.students_asked.append(student_username)
        db.session.commit()
        return jsonify({"message": "Request sent successfully!"})
    else:
        return jsonify({"error": "Student or Tutor not found"}), 404
    
@account.route("/tutorConfirmMatching", methods=["POST"])
def tutorConfirmMatching():
    tutor_username = request.args.get("tutor_username")
    student_username = request.args.get("student_username")
    print(tutor_username, student_username)
    tutor = Tutor.query.filter((Tutor.username == tutor_username)).first()
    student = Student.query.filter((Student.username == student_username)).first()
    if student and tutor:
        tutor.matched_students.append(student_username)
        student.matched_tutors.append(tutor_username)
        if student_username in tutor.students_asked:
            tutor.students_asked.remove(student_username)
        if tutor_username in student.tutors_asked:
            student.tutors_asked.remove(tutor_username)
        db.session.commit()
        return jsonify({"message": "Request sent successfully!"})
    else:
        return jsonify({"error": "Student or Tutor not found"}), 404
    
@account.route("/tutorRejectMatching", methods=["POST"])
def tutorRejectMatching():
    tutor_username = request.args.get("tutor_username")
    student_username = request.args.get("student_username")
    tutor = Tutor.query.filter((Tutor.username == tutor_username)).first()
    student = Student.query.filter((Student.username == student_username)).first()
    if student and tutor:
        if student_username in tutor.students_asked:
            tutor.students_asked.remove(student_username)
        if tutor_username in student.tutors_asked:
            student.tutors_asked.remove(tutor_username)
        db.session.commit()
        return jsonify({"message": "Request sent successfully!"})
    else:
        return jsonify({"error": "Student or Tutor not found"}), 404
    
@account.route("/studentCancelMatching", methods=["POST"])
def studentCancelMatching():
    student_username = request.args.get("student_username")
    tutor_username = request.args.get("tutor_username")
    student = Student.query.filter((Student.username == student_username)).first()
    tutor = Tutor.query.filter((Tutor.username == tutor_username)).first()
    if student and tutor:
        if tutor_username in student.tutors_asked:
            student.tutors_asked.remove(tutor_username)
        if student_username in tutor.students_asked:
            tutor.students_asked.remove(student_username)
        db.session.commit()
        return jsonify({"message": "Request sent successfully!"})
    else:
        return jsonify({"error": "Student or Tutor not found"}), 404
    
@account.route("/getStudentsAskedTutor", methods=["GET"])
def getStudentsAskedTutor():
    student_username = request.args.get("student_username")
    student = Student.query.filter((Student.username == student_username)).first()
    if student:
        asked_tutors = []
        for tutor in student.tutors_asked:
            tutor = Tutor.query.filter((Tutor.username == tutor)).first()
            if tutor:
                asked_tutors.append(
                    {
                        "username": tutor.username,
                        "nickname": tutor.nickname,
                        "edu_level": tutor.edu_level,
                        "subjects": tutor.get_subjects(),
                        "msg": tutor.msg,
                        "salary": tutor.salary,
                        "timezone": tutor.timezone,
                        "available_time": tutor.available_time,
                    }
                )
        return jsonify({"list": asked_tutors})
    else:
        return jsonify({"error": "Student not found"}), 404
    
@account.route("/getStudentMatchedTutor", methods=["GET"])
def getStudentMatchedTutor():
    student_username = request.args.get("student_username")
    student = Student.query.filter((Student.username == student_username)).first()
    if student:
        matched_tutors = []
        for tutor in student.matched_tutors:
            tutor = Tutor.query.filter((Tutor.username == tutor)).first()
            if tutor:
                matched_tutors.append(
                    {
                        "username": tutor.username,
                        "nickname": tutor.nickname,
                        "edu_level": tutor.edu_level,
                        "subjects": tutor.get_subjects(),
                        "msg": tutor.msg,
                        "salary": tutor.salary,
                        "timezone": tutor.timezone,
                        "available_time": tutor.available_time,
                    }
                )
        return jsonify({"list": matched_tutors})
    else:
        return jsonify({"error": "Student not found"}), 404
    
@account.route("/getTutorsAskedStudent", methods=["GET"])
def getTutorsAskedStudent():
    tutor_username = request.args.get("tutor_username")
    tutor = Tutor.query.filter((Tutor.username == tutor_username)).first()
    if tutor:
        asked_students = []
        for student in tutor.students_asked:
            student = Student.query.filter((Student.username == student)).first()
            if student:
                asked_students.append(
                    {
                        "username": student.username,
                        "nickname": student.nickname,
                        "grade": student.grade,
                        "timezone": student.timezone,
                        "msg": student.msg,
                    }
                )
        return jsonify({"list": asked_students})
    else:
        return jsonify({"error": "Tutor not found"}), 404
    
@account.route("/getTutorMatchedStudent", methods=["GET"])
def getTutorMatchedStudent():
    tutor_username = request.args.get("tutor_username")
    tutor = Tutor.query.filter((Tutor.username == tutor_username)).first()
    if tutor:
        matched_students = []
        for student in tutor.matched_students:
            student = Student.query.filter((Student.username == student)).first()
            if student:
                matched_students.append(
                    {
                        "username": student.username,
                        "nickname": student.nickname,
                        "grade": student.grade,
                        "timezone": student.timezone,
                        "msg": student.msg,
                    }
                )
        return jsonify({"list": matched_students})
    else:
        return jsonify({"error": "Tutor not found"}), 404