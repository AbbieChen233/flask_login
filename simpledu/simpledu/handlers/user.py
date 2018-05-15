from flask import Blueprint,render_template
from simpledu.models import User,Course

user = Blueprint('user',__name__,url_prefix='/user/<username>')

@user.route('/')
def aboutuser(username):
	
	user = User.query.filter_by(username=username).first()
	
	if user:
		return render_template('user.html',user=user)
	else:
		return render_template('404.html'),404