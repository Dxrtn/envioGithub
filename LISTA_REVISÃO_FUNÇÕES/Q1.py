def login(user, password):
    if user == 'admin' and password == 'admin':
        return True
    
email = input("Digite o email: ")
senha = input("Digite a senha: ")

login(email, senha)