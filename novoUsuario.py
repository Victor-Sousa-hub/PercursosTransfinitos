from app import db
from app.models import User
from werkzeug.security import generate_password_hash

# Criando um novo usuário admin
hashed_password = generate_password_hash('Q7812ftgzx')
new_user = User(username='admin', password=hashed_password)

db.session.add(new_user)
db.session.commit()

print("Usuário criado com sucesso!")