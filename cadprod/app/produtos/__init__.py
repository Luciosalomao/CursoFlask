from flask import Blueprint

bp = Blueprint('produtos', __name__, template_folder='templates')
from app.produtos import routes
