from flask import Blueprint
# from . import login_register

login_register = Blueprint('login_register', __name__, template_folder='templates')

from . import routes