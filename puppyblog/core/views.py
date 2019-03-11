from flask import render_template, Blueprint, request

core = Blueprint('core', __name__)

@core.route('/')
def index():
    # pass
    return render_template('index.html')

@core.route('/info')
def info():
    # pass
    return render_template('info.html')
