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
    

@main.route('/login',methods = ['GET','POST'])
def login():
    from flask_login import login_user,current_user,login_required
    #from werkzeug.security import check_password_hash
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    print("Form submitted")
    if form.validate_on_submit():
        print("Form validated")
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.password == form.password.data:
            print("User authenticated")
            login_user(user)
            flash('Logado com sucesso','seccess')
            return redirect(url_for('main.index'))
        else:
            flash('Login invalido.Verifique a usuario ou senha','danger')
    else:
        print("Form not validated")
        print(form.errors)
    
    return render_template('login.html',form = form)


@main.route('/logout')
def logout():
    from flask_login import logout_user
    logout_user()
    flash('Você saiu da sua conta', 'info')
    return redirect(url_for('main.login'))


@main.route('/texto')
def textos():
    return render_template('textos.html')

@main.route('/projetos')
def projetos():
    return render_template('projetos.html')

@main.route('/finsearch')
def finsearch():
    return render_template('finsearch.html')






        
