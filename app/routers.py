from flask import Blueprint,render_template,url_for,flash,redirect,request,send_from_directory
from app.models import User
from app import db
from app.forms import LoginForm
import time
from user_agents  import parse


main = Blueprint('main',__name__)


@main.before_request
def log_trafic():
    request_time = time.strftime("[%Y-%b-%d %H:%M]")
    client_ip = request.remote_addr
    method = request.method
    path = request.path

    log_entry = f"{request_time} {client_ip} {method} {path}"
    print("------------------Requisição recebida----------------------------------")
    print(log_entry)
    with open('app/log/trafic_log.txt','a') as log_file:
        log_file.write(log_entry + '\n')

@main.after_request
def after_request(response):
    
    status = response.status
    log_entry = f"Status da resposta: {status}"
    print("----------------------Resposta---------------------")
    print(log_entry)
    with open('app/log/trafic_log.txt','a') as log_file:
        log_file.write(log_entry +'\n')
    
    return response



@main.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    user_agent_parsed = parse(user_agent)
    
    if user_agent_parsed.is_pc:
        return render_template('index.html')
    return render_template('embreve.html')
    







        
