from os import getenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from database import db
from forms import *


class App(Flask):
    pass


# Flask app
app = App(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@{getenv("DB_HOST")}/{getenv("DB_NAME")}'
app.config['SECRET_KEY'] = getenv('SECRET_KEY', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db.init_app(app)
db.create_all(app=app)
BaseModel.set_session(db.session)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Before first request
@app.before_first_request
def before_first_request():
    # Admin user init
    if getenv('ADMIN_EMAIL') and getenv('ADMIN_PASSWORD'):
        admin = User.where(username=getenv('ADMIN_EMAIL')).first()
        if not admin:
            admin = User.create(username=getenv('ADMIN_EMAIL'), password=User.generate_password_hash(getenv('ADMIN_PASSWORD')))
            admin.save()


from views import *


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=80).then()
