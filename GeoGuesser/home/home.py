from flask import Blueprint, render_template, url_for
from ..models import User


home_bp = Blueprint('home_bp', __name__, template_folder='templates')


@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home.html', title='Home')




@home_bp.route('/users/')
def all_users():
    users = User.query.all()
    print(users)
    return render_template('users.html', title='All Users', users=users)