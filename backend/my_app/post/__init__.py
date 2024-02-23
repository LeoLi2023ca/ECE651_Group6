from flask import Blueprint
# from . import login_register

post = Blueprint('post', __name__, template_folder='templates')

from . import routes