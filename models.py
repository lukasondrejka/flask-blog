from database import db
from flask_login import UserMixin
from sqlalchemy_mixins import AllFeaturesMixin as SqlalchemyAllFeaturesMixin
from sqlalchemy_mixins.timestamp import TimestampsMixin as SqlalchemyTimestampsMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


class BaseModel(db.Model, SqlalchemyAllFeaturesMixin):
    __abstract__ = True
    pass


class TimestampsMixin(SqlalchemyTimestampsMixin):
    __abstract__ = True

    @staticmethod
    def format_datetime(sa_dt):
        dt = datetime.strptime(str(sa_dt), '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%B %d, %Y, %I:%M %p')

    @staticmethod
    def format_short_datetime(sa_dt):
        dt = datetime.strptime(str(sa_dt), '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%B %d, %Y')

    @property
    def formatted_created_at(self):
        return TimestampsMixin.format_datetime(self.created_at)

    @property
    def formatted_short_created_at(self):
        return TimestampsMixin.format_short_datetime(self.created_at)

    @property
    def formatted_updated_at(self):
        return TimestampsMixin.format_datetime(self.updated_at)

    @property
    def formatted_short_updated_at(self):
        return TimestampsMixin.format_short_datetime(self.updated_at)

    @classmethod
    def latest(cls):
        return cls.query.order_by(TimestampsMixin.created_at.desc())


class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), name='password')

    def set_password(self, password):
        self.update(password=User.generate_password_hash(password))

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def generate_password_hash(password):
        return generate_password_hash(password, method='sha256')


class Post(BaseModel, TimestampsMixin):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text)

    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    @hybrid_property
    def teaser(self):
        t = self.text if len(self.text) < 350 else self.text[:350] + "…"
        return t
