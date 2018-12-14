from flask import *
from jinja2 import TemplateNotFound

auth = Blueprint("auth", __name__, template_folder='templates', url_prefix='/auth')


@auth.route('/')
def homepage():
    return render_template("endlesspages.html")

@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/register')
def register():
    return render_template("signup.html")
