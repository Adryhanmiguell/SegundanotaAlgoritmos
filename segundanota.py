
usuarios = []
produtos = []

print('\n\n')
print('-'*50)
print('MENU PRINCIPAL')
print('-'*50)

while True:
    while True:
        print("1 - Cadastrar usuário\n" "2 - Login\n" "3 - Sair do sistema \n")
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            nome = input("\nDigite seu nome: ")
            email = input("Digite seu email: ")
            if '@gmail.com' not in email:
                while True:
                    print('\nErro, email invalido')
                    email = input("Digite seu email novamente: ")
                    if '@gmail.com' in email:
                        break
            else:
                usuarios.append(nome,email)
                print(f'usuario logado {usuarios}')

            senha = input("Digite sua senha: ")
            if len(senha) < 4:
                while True:
                    print("Senha com menos de 4 caracteres, digite novamente")
                    senha = input("Digite sua senha novamente: ")
                    if len(senha) >= 4:
                        break
        
        elif opcao == '2':
            nome = input("\nDigite seu nome: ")
            email = input("Digite seu email: ")
            if '@gmail.com' not in email:
                while True:
                    print('\nErro, email invalido')
                    email = input("Digite seu email novamente: ")
                    if '@gmail.com' in email:
                        break

            senha = input("Digite sua senha: ")
            if len(senha) < 4:
                while True:
                    print("Senha com menos de 4 caracteres, digite novamente")
                    senha = input("Digite sua senha novamente: ")
                    if len(senha) >= 4:
                        break

        while True:
            print('\n\n')
            print('-'*50)
            print('MENU ADMIN')
            print('-'*50)

            print("1 - Cadastrar usuário\n"
                "2 - Gerenciar os produtos e serviços\n"
                "3 - Cadastrar produto \n"
                "4 - Cadastrar serviço\n"
                "5 - Buscar produto/serviço \n"
                "6 - Atualizar dados do produto/serviço\n"
                "7 - Remover produto/serviço \n"
                "8 - Logout\n")
            

        #elif opcao == '3':
            #verificacao = False
            #email = input("Digite seu email: ")
            #senha = input("Digite sua senha: ")
            #print()
            
            #usuario_logado = None
            #for usuario in usuarios:
                #if email == usuario["email"] and senha == usuario["senha"]:
                    #print(f"Nome: {usuario['nome']}")
                    #print("-" * 50)
                    #verificacao = True
                    #usuario_logado = usuario
                    #break
        #elif opcao == '0':
        
        
        print('Cadrastro feito com sucesso! ')