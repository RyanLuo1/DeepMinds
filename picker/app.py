from flask import Blueprint
from flask import Flask, render_template

picker_bp = Blueprint('picker', __name__,
                      template_folder='templates',
                      static_folder='static', static_url_path='assets')


@picker_bp.route('/')
def cafe():
    return render_template("picker.html")
