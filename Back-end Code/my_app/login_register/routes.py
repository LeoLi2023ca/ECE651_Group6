from . import login_register

from flask import request, jsonify, render_template
from werkzeug.security import generate_password_hash
from flask_mail import Message, Mail
import re
import uuid
from ..models import db, Student, Tutor
# from my_app import mail, mysql

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# mail = current_app.extensions['mail']
# mysql = current_app.extensions['mysql']
mail = Mail()

@login_register.route('/')
def home():
    return "This is the login/register page"

@login_register.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    id = request.json['id']  # 'Student' or 'Tutor'
    hashed_password = generate_password_hash(password)
    token = str(uuid.uuid4())  # Generate a unique activation token
    if id == 'Student':
        model = Student
    elif id == 'Tutor':
        model = Tutor

    # Validate email format
    if not re.match(email_regex, email):
        return jsonify({'error': 'Invalid email format'}), 400
    
    # Check for duplicate username or email
    existing_student = Student.query.filter((Student.username == username) | (Student.email == email)).first()
    existing_tutor = Tutor.query.filter((Tutor.username == username) | (Tutor.email == email)).first()
    if existing_student or existing_tutor:
        return jsonify({'error': 'Username or email already exists.'}), 409
    
    # Create new student instance
    new_account = model(
        username=username,
        password=password,
        email=email,
        activation_token=token
    )
    
    # Add new student to the session and commit
    try:
        db.session.add(new_account)
        send_welcome_mail(email, token)
        db.session.commit()
        return jsonify({'message': 'Account added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@login_register.route('/delete_account', methods=['POST'])
def delete_account():
    account_identifier = request.json.get('identifier')  # Could be either username or email
    id = request.json.get('id')  # 'Students' or 'Teachers'

    # Determine the model based on the 'id' provided
    model = None
    if id == 'Student':
        model = Student
    elif id == 'Tutor':
        model = Tutor
    else:
        return jsonify({'error': 'Invalid account type'}), 400

    # Query the database for the user by username or email
    user = model.query.filter((model.username == account_identifier) | (model.email == account_identifier)).first()
    
    if user:
        try:
            # Delete the user record
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': f'Account with username/email: {account_identifier} deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Account not found'}), 404


@login_register.route('/activate')
def activate():
    token = request.args.get('token')
    if not token:
        return "Activation token is missing", 400

    # Query the database for the token
    student_user = Student.query.filter_by(activation_token=token).first()
    tutor_user = Tutor.query.filter_by(activation_token=token).first()

    if student_user:
        # Token is valid, activate the account and remove the token
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
        return "Invalid or expired activation link."
    
@login_register.route('/login', methods=['POST'])
def login():
    login_identifier = request.json['login_identifier']
    password = request.json['password']
    existing_student = Student.query.filter((Student.username == login_identifier) | (Student.email == login_identifier)).first()
    existing_tutor = Tutor.query.filter((Tutor.username == login_identifier) | (Tutor.email == login_identifier)).first()
    user = existing_student if existing_student else existing_tutor

    # Check if the user exists and the password is correct
    if user and user.password == password:
        if user.registration_completed:
            return jsonify({'message': 'Login successful!'})
        else:
            return jsonify({'error': 'Account is not activated.'}), 401
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@login_register.route('/updatePwd', methods=['POST'])
def update_password():
    username = request.json['username']
    new_password = request.json['new_password']
    existing_student = Student.query.filter((Student.username == username)).first()
    existing_tutor = Tutor.query.filter((Tutor.username == username)).first()
    user = existing_student if existing_student else existing_tutor

    if user:
        user.password = new_password
        try:
            db.session.commit()
            return jsonify({'message': 'Password updated successfully!'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'User not found'}), 404

@login_register.route('/updateStudentInfo', methods=['POST'])
def update_student_info():
    username = request.json['username']
    new_info = request.json['info']
    existing_student = Student.query.filter((Student.username == username)).first()
    if existing_student:
        existing_student.msg = new_info
        try:
            db.session.commit()
            return jsonify({'message': 'Email updated successfully!'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Student not found'}), 404
    
@login_register.route('/getStudentInfoByID', methods=['GET'])
def get_student_info_by_id():
    student_id = request.args.get('id')
    student = Student.query.filter_by(id=student_id).first()
    if student:
        return jsonify({'username': student.username, 'email': student.email, 'grade': student.grade, 'timezone': student.timezone, 'msg': student.msg})
    else:
        return jsonify({'error': 'Student not found'}), 404

def activation_token():
    return str(uuid.uuid4())

def send_welcome_mail(email, token):
    activation_url = 'http://127.0.0.1:5000/activate?token={}'.format(token)
    html_content = render_template('activation_email.html', activation_url=activation_url)
    msg = Message('Welcome to OnlineTutor', recipients=[email], html=html_content)
    # msg.body = 'Welcome to OnlineTutor! Please click the link below to activate your account:\nhttp://127.0.0.1:5000/activate?token={}'.format(token)
    with login_register.open_resource('../static/OnlineTutor.jpg') as fp:
        msg.attach('logo.png', 'image/png', fp.read(), 'inline', headers=[['Content-ID', '<OnlineTutorLogo>']])
    mail.send(msg)