from flask_sqlalchemy import SQLAlchemy
#from models import BaseModel

db = SQLAlchemy(session_options={'autocommit': True})


def init_db(app):
    db.init_app(app)
    db.create_all(app=app)
    #BaseModel.set_session(db.session)
