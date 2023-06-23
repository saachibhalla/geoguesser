

#import

from flask import(
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    current_app as app
)

from flask_login import(
    current_user,
    login_user,
    logout_user,
    login_required
)

from ..import db, bcrypt, mail
from ..models import User
from .forms import RegistrationForm
from .forms import LoginForm

#define blueprint
auth_bp = Blueprint(
    'auth_bp',
    __name__,
    url_prefix='/auth/',
    template_folder='templates'

)

#define routes

#login

@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print(current_user, "is authenticated")
        return redirect(url_for('home_bp.home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("logging user in")
            login_user(user)
            print(current_user)
            flash(' Welcom {cyrrebt_user.firstname} {current_user.lastname}!')
            return redirect(url_for('home_bp.home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html', title='User Login', form=form)

#logout
@auth_bp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home_bp.home, home'))

#register
@auth_bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, alias=form.alias.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()


        flash(f'Account has been created for {user.firstname} {user.lastname}')
        return redirect(url_for('home_bp.home'))
    return render_template('register.html', title="Register", form=form)