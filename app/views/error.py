from flask import Blueprint
from flask import render_template


app = Blueprint('errors', __name__)


@app.app_errorhandler(404)
def not_found_error(e):
    return render_template('errors/404.html')


@app.app_errorhandler(400)
def bad_request_error(e):
    return render_template('errors/400.html')


@app.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html')
