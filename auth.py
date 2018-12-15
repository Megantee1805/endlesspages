from flask import *
from jinja2 import TemplateNotFound
from wtforms import *
from db import *

bp = Blueprint("auth", __name__, template_folder='templates', url_prefix='/auth')


@bp.route('/')
def homepage():
    return render_template("auth/endlesspages.html")

@bp.route('/login')
def login():
    db = get_db()
    username = request.form("username")
    password = request.form("password")
    @bp.before_app_request
    def load_logged_in_user():
            user_id = session.get('user_id')

            if user_id is None:
                g.user = None
            else:
                g.user = get_db().execute(
                    'SELECT * FROM user WHERE id = ?', (user_id,)
                ).fetchone()
    return render_template("auth/login.html")


@bp.route('/register', methods=["GET", "POST"])
def register():
    db = get_db()
    if request.method == "POST":
        username = request.form("name")
        password = request.form("password")
        email = request.form("email")
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required'
            if error is None:
                return redirect(url_for('login'))
            return render_template("auth/signup.html")

@bp.route('/homepage')
def homepage():
    return render_template("auth/homepage.html")

@bp.route('/profile')
def profile():
    return render_template("auth/profile.html")

@bp.route('/settings')
def settings():
    return render_template("auth/settings.html")
