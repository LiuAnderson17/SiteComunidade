from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# Usar variáveis do .env
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'
ckeditor = CKEditor(app)
migrate = Migrate(app, database)

from comunidadeimpressionadora import routes