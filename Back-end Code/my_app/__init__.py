from flask import Flask
from flask_mail import Mail
from flask_mysqldb import MySQL

mail = Mail()
mysql = MySQL()

def create_app():
    app = Flask(__name__)
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
    app.config['MAIL_USERNAME'] = 'username@gmail.com'  # Your email username
    app.config['MAIL_PASSWORD'] = '########'  # Your email password
    app.config['MAIL_DEFAULT_SENDER'] = 'username@gmail.com'  # Default sender email address

    mail.init_app(app)
    mysql.init_app(app)

    from .login_register import login_register
    app.register_blueprint(login_register)

    return app