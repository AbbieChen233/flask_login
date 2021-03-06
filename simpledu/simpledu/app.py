from flask import Flask,render_template
from simpledu.config import configs
from simpledu.models import db,Course,User
from flask_migrate import Migrate
from flask_login import LoginManager

def create_app(config):
	'''可以根据传入的config名称，加载不同的配置'''
	app = Flask(__name__)
	app.config.from_object(configs.get(config))
	
	register_extensions(app)
	
	register_blueprints(app)
		
	return app
	
def register_extensions(app):
	#SQLAlchemy的初始方式改为使用init_app
	#连接数据库与flask
	db.init_app(app)
	
	#将db注册到app上
	Migrate(app,db)
	
	login_manager = LoginManager()
	login_manager.init_app(app)
	
	@login_manager.user_loader
	def user_loader(id):
		return User.query.get(id)
		
	login_manager.login_view = 'front.login'
	
def register_blueprints(app):
	from .handlers import front,course,admin,user
	app.register_blueprint(front)
	app.register_blueprint(course)
	app.register_blueprint(admin)
	app.register_blueprint(user)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	