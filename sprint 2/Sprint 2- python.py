import re

controle = [1,2,3,4,5,6] #criação de uma lista para controle
positivo = ['sim','s','ss','sss','si'] #lista para controle

usuarios = {} #criação de um dicionário para armazenamento de dados do usuarios

def confirmacao(email, senha): #criando uma função para reutilização futura do codigo
    verificacao = input("As informações estão corretas? ").lower()
    if (verificacao in positivo):
        print('Cadastro finalizado. \n')
        usuarios[email] = senha
        return(0)
    else:
        print('Digite as informações novamente.')
        return(1)

while True: #inicia um loop infinito (ter cuidado para não ficar em um loop infinito, sempre ter uma rota de escape)
    print('Digite 1 caso queira saber os canais de contato disponíveis.') #imprime na tela um texto
    print('Digite 2 caso queira se cadastrar.') #imprime na tela um texto
    print('Digite 3 caso queira saber se atende aos requisitos.') #imprime na tela um texto
    print('Digite 4 caso queira saber o andamento do seu atendimento.') #imprime na tela um texto
    print('Digite 5 caso queira agendar seu atendimento.')
    print('Digite 6 caso queira sair.') #imprime na tela um texto

    try:
        escolha = int(input('Digite a opção desejada: ')) #pede para o usuário digitar um número inteiro

        if (escolha in controle): #verifica se o que o usuário digitou está dentro da lista
            if(escolha == 1): #verifica se o que o usuário digitou é igual a 1 (informa os canais disponiveis para contato)
                print('\nE-mail: ongTDB@StartUpados.com.br')
                print('Telefone: 12345-6789')
                print('WhatsApp: 11 12345-6789\n')

            elif(escolha == 2): #verifica se o que o usuário digitou é igual a 2 (inicia cadastro geral)
                print('Digite 1 caso queira se cadastrar como beneficiário.')
                print('Digite 2 caso queira se cadastrar como dentista.')
                print('Digite 3 caso queira se cadastrar como voluntário.')
                try:
                    resposta = int(input())
                    if (resposta == 1): # Inicia Cadastro de beneficiário
                        while True:
                            nome = input('Digite seu nome: ') #entrada de dados
                            email = input('Digite seu e-mail: ') #entrada de dados
                            if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                                print('E-mail inválido.')
                            else:
                                telefone = int(input('Digite seu telefone: ')) #entrada de dados numéricos
                                idade = int(input('Digite a sua idade: '))
                                senha = input('Digite uma senha forte: ') #entrada de dados
                                senhaRedigitada = input('Redigite sua senha: ') #entrada de dados
                                if (senha != senhaRedigitada):
                                    print('Erro: as senhas devem ser iguais \n')
                                else:
                                    print('\n' + nome)
                                    print(email)
                                    print(telefone)
                                    print(idade , '\n')
                                    if(confirmacao(email, senha) == 0):
                                        break
                    elif(resposta == 2): # Inicia Cadastro de dentista
                        while True:
                            nome = input ('Digite seu nome: ') #entrada de dados
                            CRO = input ('Digite seu C.R.O: ')
                            email = input('Digite seu e-mail: ') #entrada de dados
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
                                    print('\n' + nome)
                                    print(CRO)
                                    print(email)
                                    print(telefone)
                                    print(endereco , '\n')
                                    if(confirmacao(email, senha) == 0):
                                        break
                    elif(resposta == 3): # Inicia Cadastro de voluntário
                        while True:
                            nome = input ('Digite seu nome: ') #entrada de dados
                            email = input('Digite seu e-mail: ') #entrada de dados
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
                                    if(confirmacao(email, senha) == 0):
                                        break
                    else:
                        print('Por favor, digite uma opção válida.')       
                except ValueError:
                    print('Digite apenas números, por favor. \n')

            elif (escolha == 3): #verifica se o que o usuário digitou é igual a 3 (entra para a parte de verificação de requisitos)
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

            elif(escolha == 4): #verifica se o que o usuário digitou é igual a 4 (entra para a parte de verificação de atendimento)
                print('Você já possui cadastro?')
                verificacao = input('').lower()
                if (verificacao in positivo):
                    email = input('Digite seu e-mail:')
                    senha = input('Digite sua senha:')
                    if (email in usuarios and usuarios[email] == senha):
                        print('O login foi realizado com sucesso.')
                        print('Atendimento em processo, por favor aguarde. \n')
                    else:
                        print('E-mail ou senha incorretos.\n')
                else:
                    print('Por favor, realize seu cadastro.\n')

            elif(escolha == 5): #verifica se o que o usuário digitou é igual a 5 (entra para a marcação de consulta)
                print('Você já possui cadastro?')
                verificacao = input('').lower()
                if (verificacao in positivo):
                    email = input('Digite seu e-mail:')
                    senha = input('Digite sua senha:')
                    if (email in usuarios and usuarios[email] == senha):
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
                        print('E-mail ou senha incorretos. \n')   
                else:
                    print('Por favor, realize seu cadastro. \n')
            else:
                break
        else:
            print('Por favor, digite uma opção válida! \n')

    except ValueError:
        print('Por favor, digite um número.\n')