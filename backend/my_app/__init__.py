from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from my_app.models import db

mail = Mail()

    
# app.register_blueprint(account)
# app.register_blueprint(post)
def create_app():
    app = Flask(__name__)
    CORS(app)
    # CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
    # Configure MySQL connection
    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'root'
    # app.config['MYSQL_PASSWORD'] = 'rainchoi228'
    # app.config['MYSQL_DB'] = 'OnlineTutor'

    # Configure SQLAlchemy connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rainchoi228@localhost/OnlineTutor'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Flask-Mail configuration
    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # The mail server
    # app.config['MAIL_PORT'] = 587  # The mail server port
    # app.config['MAIL_USE_TLS'] = True  # Use TLS
    # app.config['MAIL_USE_SSL'] = False  # Use SSL (alternative to TLS)
    # app.config['MAIL_USERNAME'] =   # Your email username
    # app.config['MAIL_PASSWORD'] =   # Your email password
    # app.config['MAIL_DEFAULT_SENDER'] =   # Default sender email address

    mail.init_app(app)
    db.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app