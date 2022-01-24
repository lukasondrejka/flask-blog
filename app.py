from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import database
from forms import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = "SECRET_KEY"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
BaseModel.set_session(db.session)

login_manager = LoginManager()
login_manager.init_app(app)


from views import *


if __name__ == '__main__':
    # app.run(debug=False)
    app.run(debug=True, use_reloader=True)
