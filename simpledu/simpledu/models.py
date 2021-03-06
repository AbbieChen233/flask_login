from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



#这里不再传入app

db = SQLAlchemy()

	
class Base(db.Model):
	__abstract__ = True
	created_at = db.Column(db.DateTime,default=datetime.utcnow)
	updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
	
	
class User(Base,UserMixin):
	__tablename__ = 'user'
	
	#用数值表示角色
	ROLE_USER = 10
	ROLE_STAFF = 20
	ROLE_ADMIN = 30
	
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(32),unique=True,index=True,nullable=False)
	publish_course = db.relationship('Course')
	email = db.Column(db.String(128),unique=True,index=True,nullable=False)
	_password = db.Column('password',db.String(256),nullable=False)
	role = db.Column(db.Integer,default=ROLE_USER)
	
	def __repr__(self):
		return '<User:{}>'.format(self.username)

	@property
	def password(self):
		'''python风格的getter'''
		return self._password
		
		
	@password.setter
	def password(self,password):
		self._password = generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self._password,password)
		
	@property
	def is_admin(self):
		return self.role == ROLE_ADMIN
		
	@property
	def is_staff(self):
		return self.role == ROLE_STAFF
	
		
class Course(Base):
	__tablename__ = 'course'
	
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(128),unique=True,index=True,nullable=False)
	#ondelete='CASCADE'表示如果用户被删除了，那么他的课程也会被删除
	
	author_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'))
	author = db.relationship('User',uselist=False)
