from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Length,Email,EqualTo,Required
from simpledu.models import db,User
from wtforms import ValidationError
from flask import flash
import re

class RegisterForm(FlaskForm):
	username = StringField('Username',validators=[Required(),Length(3,24)])
	email = StringField('email',validators=[Required(),Email()])
	password = PasswordField('password',validators=[Required(),Length(6,24)])
	repeat_password = PasswordField('password',validators=[Required(),Length(6,24),EqualTo('password')])
	submit = SubmitField('提交')
	
	#根据表单提交的数据创建用户
	def create_user(self):
		user = User()
		user.username = self.username.data
		user.email = self.email.data
		user.password = self.password.data
		db.session.add(user)
		db.session.commit()
		return user
		
	def validate_username(self,field):
		user = User.query.filter_by(username=field.data).first()
		if user:
			raise ValidationError('用户名已经存在')
			
			
		pattern = re.compile(r'[\W]+')
		m = re.search(pattern,field.data)
		if not user and m:
			flash('用户名只能由字母和数字组成')
			raise ValidationError('用户名只能由字母和数字组成')
			
	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('邮箱已经存在')


class LoginForm(FlaskForm):
	email = StringField('Username',validators=[Required(),Length(3,24)])
	password = PasswordField('password',validators=[Required(),Email()])
	remember_me = BooleanField('记住我')
	submit = SubmitField('submit')
	

	def validate_username(self,field):
		if not User.query.filter_by(username=field.data).first() and field.data:
			raise ValidationError('用户名未注册')

	def validate_password(self,field):
		user = User.query.filter_by(email=self.email.data).first()
		if user and not user.check_password(user.password):
			raise ValidationError('密码错误')
			
	
	
	
	
	
	