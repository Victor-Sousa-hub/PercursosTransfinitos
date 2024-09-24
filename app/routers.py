from flask import Blueprint,render_template,url_for,flash,redirect,request,send_from_directory
from app.models import User
from app import db
from app.forms import LoginForm
import time
from user_agents  import parse


main = Blueprint('main',__name__)


@main.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    user_agent_parsed = parse(user_agent)
    
    if user_agent_parsed.is_pc:
        return render_template('index.html')
    return render_template('embreve.html')
    







        
