import re

controle = [1,2,3,4,5,6,7,8,9,10] #criação de uma lista para controle
positivo = ['sim','s','ss','sss','si'] #lista para controle

email_logado = None

lista_usuarios = [] #criação de uma lista para armazenamento de decionarios de usuario

usuario = {}

def confirmacao(proficao,nome,email,senha,telefone,idade,sexo,endereco,cro): #criando uma função para reutilização futura do codigo
    verificacao = input("As informações estão corretas? ").lower()
    if(verificacao in positivo):
        if (proficao == "beneficiario" ):
            usuario = { #criando um dicionario para manipulaçao e armazenamendo de dados
                'Nome':nome,
                'Idade': idade,
                'Sexo':sexo,
                'Telefone': telefone,
                'Cadastro': proficao,
                'Email':email,
                'Senha':senha
            }
            lista_usuarios.append(usuario)
        elif(proficao == "dentista"):
            usuario = {
                'Nome':nome,
                'CRO': cro,
                'Endereço':endereco,
                'Telefone': telefone,
                'Cadastro': proficao,
                'Email':email,
                'Senha':senha,
            }
            lista_usuarios.append(usuario)
        elif(proficao == "voluntario"):
            usuario = {
                'Nome':nome,
                'Telefone': telefone,
                'Endereço':endereco,
                'Cadastro': proficao,
                'Email':email,
                'Senha':senha,
            }
            lista_usuarios.append(usuario)
        print('\nCadastro linalizado \n')
        return(0)
    else:
        return(1)   

while True: #inicia um loop infinito (ter cuidado para não ficar em um loop infinito, sempre ter uma rota de escape)
    print('Digite 1 caso queira saber os canais de contato disponíveis.') #imprime na tela um texto
    print('Digite 2 caso queira se cadastrar.') #imprime na tela um texto
    print('Digite 3 caso queira logar na sua conta.') #imprime na tela um texto
    print('Digite 4 caso queria ver seus dados') #imprime na tela um texto
    print('Digite 5 caso queria alterar seus dados') #imprime na tela um texto
    print('Digite 6 caso queria excluir seus dados') #imprime na tela um texto
    print('Digite 7 caso queira saber se atende aos requisitos.') #imprime na tela um texto
    print('Digite 8 caso queira saber o andamento do seu atendimento.') #imprime na tela um texto
    print('Digite 9 caso queira agendar seu atendimento.') #imprime na tela um texto
    print('Digite 10 caso queira sair.') #imprime na tela um texto

    try:
        escolha = int(input('Digite a opção desejada: ')) #pede para o usuário digitar um número inteiro

        if (escolha in controle): #verifica se o que o usuário digitou está dentro da lista
            if(escolha == 1): #verifica se o que o usuário digitou é igual a 1 (informa os canais disponiveis para contato)
                print('\nE-mail: ongTDB@StartUpados.com.br')
                print('Telefone: 12345-6789')
                print('WhatsApp: 11 12345-6789\n')
            elif(escolha == 2): #verifica se o que o usuário digitou é igual a 2 (inicia cadastro geral)
                print('\nDigite 1 caso queira se cadastrar como beneficiário.')
                print('Digite 2 caso queira se cadastrar como dentista.')
                print('Digite 3 caso queira se cadastrar como voluntário.\n')
                try:
                    resposta = int(input('Digite a opção desejada: '))
                    if (resposta == 1): # Inicia Cadastro de beneficiário
                        while True:
                            nome = input('Digite seu nome: ') #entrada de dados
                            email = input('Digite seu e-mail: ').lower() #entrada de dados
                            if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                                print('E-mail inválido.')
                            else:
                                telefone = int(input('Digite seu telefone: ')) #entrada de dados numéricos
                                idade = int(input('Digite a sua idade: '))
                                sexo = input('Digite seu sexo: ')
                                senha = input('Digite uma senha forte: ') #entrada de dados
                                senhaRedigitada = input('Redigite sua senha: ') #entrada de dados
                                if (senha != senhaRedigitada):
                                    print('Erro: as senhas devem ser iguais \n')
                                else:
                                    print('\nNome: ' + nome)
                                    print("Sexo: " + sexo) 
                                    print("Telefone: " , telefone)
                                    print("Idade: " , idade )
                                    print("Email: " + email + '\n')
                                    if(confirmacao("beneficiario",nome,email,senha,telefone,idade,sexo,None,None) == 0):
                                        break
                    elif(resposta == 2): # Inicia Cadastro de dentista
                        while True:
                            nome = input ('Digite seu nome: ') #entrada de dados
                            CRO = input ('Digite seu C.R.O: ')
                            email = input('Digite seu e-mail: ').lower() #entrada de dados
                            if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                                print('E-mail inválido.')
                            else:
                                telefone = int(input('Digite seu telefone: ')) #entrada de dados numéricos
                                endereco = input('Digite seu endereço: ')
                                senha = input('Digite uma senha forte: ') #entrada de dados
                                senhaRedigitada = input('Redigite sua senha: ') #entrada de }dados
                                if (senha != senhaRedigitada):
                                    print('Erro: as senhas devem ser iguais. \n')
                                else:
                                    print('\nNome: ' + nome)
                                    print("CRO: ", CRO)
                                    print("Email: " +email)
                                    print("Telefone: " ,telefone)
                                    print("Endereço: " + endereco , '\n')
                                    if(confirmacao("dentista",nome,email,senha,telefone,None,None,endereco,CRO) == 0):
                                        break
                    elif(resposta == 3): # Inicia Cadastro de voluntário
                        while True:
                            nome = input ('Digite seu nome: ') #entrada de dados
                            email = input('Digite seu e-mail: ').lower() #entrada de dados
                            if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                                print('E-mail inválido.')
                            else:
                                telefone = int(input('Digite seu telefone: ')) #entrada de dados numéricos
                                endereco = input('Digite seu endereço: ') #entrada de dados
                                senha = input('Digite uma senha forte: ') #entrada de dados
                                senhaRedigitada = input('Redigite sua senha: ') #entrada de dados
                                if (senha != senhaRedigitada):
                                    print('Erro: as senhas devem ser iguais. \n')                                  
                                else:
                                    print('\n' + nome)
                                    print(email)
                                    print(telefone)
                                    print(endereco , '\n')
                                    if(confirmacao("voluntario",nome,email,senha,telefone,None,None,endereco,None) == 0):
                                        break
                    else:
                        print('Por favor, digite uma opção válida.')       
                except ValueError:
                    print('Digite apenas números, por favor. \n')
            elif(escolha == 3):
                email_digitado = input("Digite seu email: ")
                senha_digitada = input("Digite sua senha: ")
                for i in range(len(lista_usuarios)):
                        if(lista_usuarios[i]['Email'] == email_digitado and lista_usuarios[i]['Senha'] == senha_digitada):
                            email_logado = email_digitado
                            print("Login realizado com sucesso!")
                        else:
                            print("Email ou senha não encontrado")
            elif(escolha == 4):
                indice = -1
                for i in range(len(lista_usuarios)):
                    if(lista_usuarios[i]['Email'] == email_logado):
                        indice = i
                if(indice != -1):
                    print('\n')
                    for chave,valor in lista_usuarios[indice].items():
                        print(f"{chave}:{valor}")
                    print('\n')
                else:
                    print("Por favor realize o login\n")
            elif(escolha == 5):
                indice = -1
                for i in range(len(lista_usuarios)):
                    if(lista_usuarios[i]['Email'] == email_logado):
                        indice = i
                if(indice != -1):
                    if(lista_usuarios[i]['Cadastro'] == "beneficiario"):
                        try:
                            print(f"Nome: {lista_usuarios[i]['Nome']}")
                            novo_nome = input("Digite o novo nome: ")
                            print(f"Idade: {lista_usuarios[i]['Idade']}")
                            nova_idade = int(input("Digite a nova idade: "))
                            print(f"Sexo: {lista_usuarios[i]['Sexo']}")
                            novo_sexo = input("Digite o novo sexo: ")
                            print(f"Telefone: {lista_usuarios[i]['Telefone']}")
                            novo_telefone = int(input("Digite o novo telefone: "))
                            while True:
                                print(f"Email: {lista_usuarios[i]['Email']}")
                                novo_email = input("Digite o novo email: ")
                                if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                                    print('E-mail inválido. \n')
                                else:
                                    break
                            print(f"Senha: {lista_usuarios[i]['Senha']}")
                            nova_senha = input("Digite o nova senha: ")
                            lista_usuarios[indice]['Nome'] = novo_nome
                            lista_usuarios[indice]['Idade'] = nova_idade
                            lista_usuarios[indice]['Sexo'] = novo_sexo
                            lista_usuarios[indice]['Telefone'] = novo_telefone
                            lista_usuarios[indice]['Email'] = novo_email
                            lista_usuarios[indice]['Senha'] = nova_senha
                        except ValueError:
                            print("digite apenas numeros")
                    elif(lista_usuarios[i]['Cadastro'] == "dentista"):
                        try:
                            print(f"Nome: {lista_usuarios[i]['Nome']}")
                            novo_nome = input("Digite o novo nome: ")
                            print(f"CRO: {lista_usuarios[i]['CRO']}")
                            novo_cro = int(input("Digite a novo CRO: "))
                            print(f"Endereço: {lista_usuarios[i]['Endereço']}")
                            novo_endereco = input("Digite o novo endereço: ")
                            print(f"Telefone: {lista_usuarios[i]['Telefone']}")
                            novo_telefone = int(input("Digite o novo telefone: "))
                            while True:
                                print(f"Email: {lista_usuarios[i]['Email']}")
                                novo_email = input("Digite o novo email: ")
                                if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                                    print('E-mail inválido. \n')
                                else:
                                    break
                            print(f"Senha: {lista_usuarios[i]['Senha']}")
                            nova_senha = input("Digite o nova senha: ")
                            lista_usuarios[indice]['Nome'] = novo_nome
                            lista_usuarios[indice]['CRO'] = novo_cro
                            lista_usuarios[indice]['Enderoço'] = novo_endereco
                            lista_usuarios[indice]['Telefone'] = novo_telefone
                            lista_usuarios[indice]['Email'] = novo_email
                            lista_usuarios[indice]['Senha'] = nova_senha
                        except ValueError:
                            print("digite apenas numeros")
                    elif(lista_usuarios[i]['Cadastro'] == "voluntario"):
                        try:
                            print(f"Nome: {lista_usuarios[i]['Nome']}")
                            novo_nome = input("Digite o novo nome: ")
                            print(f"Endereço: {lista_usuarios[i]['Endereço']}")
                            novo_endereco = input("Digite o novo endereço: ")
                            print(f"Telefone: {lista_usuarios[i]['Telefone']}")
                            novo_telefone = int(input("Digite o novo telefone: "))
                            while True:
                                print(f"Email: {lista_usuarios[i]['Email']}")
                                novo_email = input("Digite o novo email: ")
                                if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                                    print('E-mail inválido. \n')
                                else:
                                    break
                            print(f"Senha: {lista_usuarios[i]['Senha']}")
                            nova_senha = input("Digite o nova senha: ")
                            lista_usuarios[indice]['Nome'] = novo_nome
                            lista_usuarios[indice]['Enderoço'] = novo_endereco
                            lista_usuarios[indice]['Telefone'] = novo_telefone
                            lista_usuarios[indice]['Email'] = novo_email
                            lista_usuarios[indice]['Senha'] = nova_senha
                        except ValueError:
                            print("digite apenas numeros")
                else:
                    print("Por favor realize o login\n")
            elif(escolha == 6):
                indice = -1
                for i in range(len(lista_usuarios)):
                    if(lista_usuarios[i]['Email'] == email_logado):
                        indice = i
                    else:
                        print("Por favor realize o login")
                if(indice != -1):
                    lista_usuarios.pop(indice)
                else:
                    print("Você não está logado")
            elif (escolha == 7): #verifica se o que o usuário digitou é igual a 7 (entra para a parte de verificação de requisitos)
                try:
                    idade = int(input('Digite sua idade: ')) #pergunta para o usuário
                    sexo = input('Digite seu sexo: ') #pergunta para o usuário
                    controleMasc = ['homem','macho','masculino','m','menino'] #cria uma lista para múltiplas respostas do usuário
                    controleFem = ['mulher','menina','fêmea','feminino','f'] #cria uma lista para múltiplas respostas do usuário
                    if (idade <= 17): #verifica se o que o usuário digitou é igual ou menor que 17
                        print('Você atende aos requisitos.\n')
                    elif (idade > 17 and sexo in controleFem): #verifica se o que o usuário digitou é maior que 17 e está dentro do controleFem
                        print('Você atende aos requisitos.\n')
                    else:
                        print('Você não atende aos requisitos.\n')
                except ValueError:
                    print('Digite uma informação válida.')
            elif(escolha == 8): #verifica se o que o usuário digitou é igual a 8 (entra para a parte de verificação de atendimento)
                if (email_logado != None ):
                    print('Atendimento em processo, por favor aguarde. \n')
            elif(escolha == 9): #verifica se o que o usuário digitou é igual a 9 (entra para a marcação de consulta)
                if (email_logado != None):
                    print('O login foi realizado com sucesso. \n')
                    while True:
                        print('Digite o dia, o mês e a hora que você quer agendar sua consulta.')
                        try:                               
                            dia = int(input('Dia: '))
                            mes = int(input('Mês: '))
                            hora = float(input('Hora: '))
                            if(0 < dia <= 31 and 0 < mes <= 12 and 7 <= hora <= 19):
                                print('Agendado!\n')
                                break
                            else:
                                print('Algo deu errado. Tente novamente.\n')
                        except ValueError:
                            print('Digite apenas números.\n')     
            else:
                break
        else:
            print('Por favor, digite uma opção válida! \n')
    except ValueError:
        print('Por favor, digite um número. \n')