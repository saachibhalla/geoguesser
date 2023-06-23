from dotenv import load_dotenv
load_dotenv()

from flask import Flask

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.login_message_category = 'info'


def create_app():
 app = Flask(__name__)
 app.config.from_object('config.'+os.environ.get('FLASK_ENV').capitalize())
 print(app.config)

 db.init_app(app)
 bcrypt.init_app(app)
 login_manager.init_app(app)
 mail.init_app(app)

 with app.app_context():
    from .home import home
    from .auth import auth
    app.register_blueprint(home.home_bp)
    app.register_blueprint(auth.auth_bp)
    
 return app