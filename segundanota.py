adm = []
usuarios = []
produtos = []

print('\n\n')
print('-'*50)
print('MENU PRINCIPAL')
print('-'*50)

while True:
    login = input('digite seu email: ')
    while '@gmail.com' not in login:
        login = input('email invalido, tente novamente: ')

    senha = input('digite sua senha: ')
    while len(senha) < 4:
        senha = input('digite sua senha novamente com mais de 4 caracteres: ')
    break
    
print('Login feito com sucesso! ')