from flask import Blueprint
from app.models import db
from app.models.user import User


app = Blueprint('user', __name__, url_prefix='/users')


@app.route('/count')
def show_users_count():
    user_cnt = User.query.count()
    # user_cnt = len(User.query.all())
    # user_cnt = db.session.query(User).count()
    return str(user_cnt)
