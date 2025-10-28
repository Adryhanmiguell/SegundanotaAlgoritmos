usuario = []
admin = []
produtos = []

while True:
    while True:
        print("")
        print('-'*50)
        print('- - - - - - - - - MENU PRINCIPAL - - - - - - - - -')
        print('-'*50)
        print(
            "1 - Cadastrar usuário \n"
            "2 - Cadastrar administrador \n"
            "3 - Login \n" 
            "4 - Sair \n"
            )
        opcao = int(input("\nOpção: "))
        
        if opcao == 1:
            nome = input("\nNome: ")
            email = input("Email: ")

            while '@gmail.com' not in email:
                print('\nEmail invalido !')
                email = input("Digite novamente: ")
                break

            senha = input("Senha: ")
            while len(senha) < 4:
                print("Senha com menos de 4 caracteres, digite novamente")
                senha = input("Digite sua senha novamente: ")
                break

            usuario.append(nome)
            usuario.append(email)
            usuario.append(senha)   
            print("\nUsuario cadastradado com sucesso.") 
            break

        elif opcao == 2:
            nome = input("\nNome: ")
            email = input("Email: ")

            while '@gmail.com' not in email:
                print('\nEmail invalido !')
                email = input("Digite novamente: ")
                break

            senha = input("Senha: ")
            while len(senha) < 4:
                print("Senha com menos de 4 caracteres, digite novamente")
                senha = input("Digite sua senha novamente: ")
                break

            admin.append(nome)
            admin.append(email)
            admin.append(senha)   
            print("\nAdministrador cadastradado com sucesso.") 

        
        elif opcao == 3:
            email = input("\nEmail: ")
            senha = input("Senha: ")
            
            if senha and email in usuario:
                while True:
                    print('')
                    print('-'*50)
                    print('- - - - - - - - - MENU USUARIO - - - - - - - - -')
                    print('-'*50)
                    print(
                    "1 - Comprar produtos e agendar serviços\n"
                    "2 - Logout\n"
                    )
                    opcao = input("Opção: ")
                    break



            elif senha and email in admin:
                while True:
                    print('')
                    print('-'*50)
                    print('- - - - - - - - - MENU ADMIN - - - - - - - - -')
                    print('-'*50)
                    print(
                        "1 - Gerenciar os produtos e serviços\n"
                        "2 - Cadastrar produto \n"
                        "3 - Cadastrar serviço\n"
                        "4 - Buscar produto/serviço \n"
                        "5 - Atualizar dados do produto/serviço\n"
                        "6 - Remover produto/serviço \n"
                        "7 - Logout\n"
                    )
                    opcao = input("Opção: ")

            else:
                print("Credenciais não encontradas !") 


# se os dados estiver igual vai logar no primeiro if, tem que arrumar um jeito de nao poder ter as infos iguais