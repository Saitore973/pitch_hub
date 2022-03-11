from flask import Blueprint
author = Blueprint('auth', __name__)

from . import views