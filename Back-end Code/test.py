from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from flask_mail import Mail, Message
import re
import uuid

# Create a Flask app
def create_app():
    app = Flask(__name__)
    CORS(app)
    # Configure MySQL connection
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'rainchoi228'
    app.config['MYSQL_DB'] = 'OnlineTutor'

    # Flask-Mail configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # The mail server
    app.config['MAIL_PORT'] = 587  # The mail server port
    app.config['MAIL_USE_TLS'] = True  # Use TLS
    app.config['MAIL_USE_SSL'] = False  # Use SSL (alternative to TLS)
    app.config['MAIL_USERNAME'] = 'choichonghou@gmail.com'  # Your email username
    app.config['MAIL_PASSWORD'] = 'dtuzsadcpnotmmqy'  # Your email password
    app.config['MAIL_DEFAULT_SENDER'] = 'choichonghou@gmail.com'  # Default sender email address
    return app

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

app = create_app()

mail = Mail(app)

mysql = MySQL(app)

# Route for adding a new student
@app.route('/register', methods=['POST'])
def add_student():
    # Get data from request
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    # Hash the password for security
    hashed_password = generate_password_hash(password)
    token = activation_token()
    # Create a cursor
    cur = mysql.connection.cursor()
    try:
        # Check for duplicate username or email
        if not re.match(email_regex, email):
            return jsonify({'error': 'Invalid email format'}), 400
        
        cur.execute("SELECT * FROM Students WHERE username = %s OR email = %s", (username, email))
        if cur.fetchone():
            # Found a duplicate
            return jsonify({'error': 'Username or email already exists.'}), 409

        # No duplicates found, proceed to insert
        cur.execute("INSERT INTO Students(username, password, email, activation_token) VALUES (%s, %s, %s, %s)", (username, password, email, token))
        
        # Commit to DB
        send_welcome_mail(email, token)
        mysql.connection.commit()
        
        return jsonify({'message': 'Student added successfully!'}), 201
    except Exception as e:
        # In case of any exception, rollback the transaction
        mysql.connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        # Close connection
        cur.close()

# Route for adding a new tutor
@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    # Get data from request
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    # Hash the password for security
    hashed_password = generate_password_hash(password)
    token = activation_token()
    # Create a cursor
    cur = mysql.connection.cursor()
    try:
        # Check for duplicate username or email
        if not re.match(email_regex, email):
            return jsonify({'error': 'Invalid email format'}), 400
        
        cur.execute("SELECT * FROM Teachers WHERE username = %s OR email = %s", (username, email))
        if cur.fetchone():
            # Found a duplicate
            return jsonify({'error': 'Username or email already exists.'}), 409

        # No duplicates found, proceed to insert
        cur.execute("INSERT INTO Teachers(username, password, email) VALUES (%s, %s, %s, %s)", (username, password, email, token))
        
        # Commit to DB
        mysql.connection.commit()
        return jsonify({'message': 'Teacher added successfully!'}), 201
    except Exception as e:
        # In case of any exception, rollback the transaction
        mysql.connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        # Close connection
        cur.close()

@app.route('/delete_account', methods=['POST'])
def delete_account(id='Students'):
    # Extracting username or email from request data
    account_identifier = request.json.get('identifier')  # Could be either username or email

    cur = mysql.connection.cursor()

    # Assuming 'username' and 'email' are in the same table and unique
    sql = ""
    if id == 'Students':
        sql = "DELETE FROM Students WHERE username = %s OR email = %s"
    elif id == 'Teachers':
        sql = "DELETE FROM Teachers WHERE username = %s OR email = %s"
    else:
        return jsonify({'error': 'Invalid account type'}), 400
    # sql = "DELETE FROM Students WHERE username = %s OR email = %s"
    affected_count = cur.execute(sql, (account_identifier, account_identifier))
    mysql.connection.commit()
    cur.close()

    if affected_count:
        return jsonify({'message': 'Account with username/email:{} deleted successfully'.format(account_identifier)}), 200
    else:
        return jsonify({'error': 'Account not found'}), 404

@app.route('/activate')
def activate_account():
    token = request.args.get('token')
    print(token)
    cur = mysql.connection.cursor()
    # Query the database for the token and check expiration
    cur.execute("SELECT * FROM Students WHERE activation_token = %s", (token,))
    user = cur.fetchone()
    
    if user:
        # Token is valid, activate the account and remove the token
        cur.execute("UPDATE Students SET registration_completed = TRUE, activation_token = NULL WHERE student_id = %s", (user[0],))
        mysql.connection.commit()
        return "Account activated successfully!"
    else:
        return "Invalid or expired activation link."
    
@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Students WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    if user and user[2] == password and user[5] == True:
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

def activation_token():
    return str(uuid.uuid4())

def send_welcome_mail(email, token):
    activation_url = 'http://127.0.0.1:5000/activate?token={}'.format(token)
    html_content = render_template('activation.html', activation_url=activation_url)
    msg = Message('Welcome to OnlineTutor', recipients=[email], html=html_content)
    # msg.body = 'Welcome to OnlineTutor! Please click the link below to activate your account:\nhttp://127.0.0.1:5000/activate?token={}'.format(token)
    with app.open_resource('./OnlineTutor.jpg') as fp:
        msg.attach('logo.png', 'image/png', fp.read(), 'inline', headers=[['Content-ID', '<OnlineTutorLogo>']])
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)