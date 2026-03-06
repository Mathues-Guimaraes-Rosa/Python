controle = [1,2,3,4,5,6] #criação de uma lista para controle
positivo = ['sim','s','ss','Sim','S','SS'] #lista para controle
negativo = ['nao','n','nn','não','Nao','N'] #lista para controle

while True: #inicia um loop infinito (ter cuidado para não ficar um loop infinito mesmo, sempre ter uma rota de escape)
    print('Digite 1 caso queira saber os canais de contato disponiveis.') #imprime na tela um texto
    print('Digite 2 caso queira se cadastrar.') #imprime na tela um texto
    print('Digite 3 caso queira saber se atente aos requesitos.') #imprime na tela um texto
    print('Digite 4 caso queira saber se o andameto do seu atendimento.') #imprime na tela um texto
    print('Digite 5 caso queira agendar seu atendimento.')
    print('Digite 6 caso queira sair.') #imprime na tela um texto

    escolha = int(input('Digite o número: ')) #pede para o usuário digitar um número inteiro

    if (escolha in controle): #verifica se o que o usuário digitou esta dentro da lista
        if(escolha == 1): #verifica se o que usuário digitou é igual a 1
            print('')
            print('E-mail: ongTDB@StartUpados.com.br')
            print('Telefone: 12345-6789')
            print('Whatsapp: 11 12345-6789')
            print('')
        elif(escolha == 2): #verifica se o que usuário digitou é igual a 2
            print('Digite 1 caso não tenha cadastro.')
            print('Digite 2 caso queira se cadastra como dentista.')
            print('Digite 3 caso queria se cadastrar com voluntario.')
            resposta = int(input())
            if (resposta == 1):
                nome = input ('Digite seu nome: ') #entrada de dados
                email = input('Digite seu e-mail: ') #entrada de dados
                senha = input('Digite uma senha forte: ') #entrada de dados
                telefone = int(input('Digite seu telefone: ')) #entrada de dados de números inteiros
                idade = int(input('Digite a sua idade: '))
                while True: #loop
                    print(f'{nome}, está correto?') #pergunta aou usuário se ele digitou o nome Certo
                    resposta = input() #pede uma resposta
                    if(resposta in positivo): #vê se a resposta está na lista (positivo)
                        break
                    elif(resposta in negativo): #vê se a resposta está na lista (negativo)
                        print('Certo, digite novamente.')
                        nome = input ('Digite seu nome: ') #pede para o usuário corrigir o nome
                        print(nome)
                while True:
                    print(f'{email}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, Digite novamente.')
                        email = input ('Digite seu e-mail: ')
                        print(email)
                while True:
                    print(f'{telefone}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, Digite novamente.')
                        telefone = int(input('Digite seu telefone: '))
                        print(telefone)
                while True:
                    print(f'{idade}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, Digite novamente.')
                        idade = int(input('Digite seu telefone: '))
                        print(idade)
                print('Cadastro finalizado')
            elif(resposta == 2):
                nome = input ('Digite seu nome: ') #entrada de dados
                email = input('Digite seu e-mail: ') #entrada de dados
                senha = input('Digite uma senha forte: ')
                telefone = int(input('Digite seu telefone: ')) #entrada de dados de números inteiros
                endereço = int(input('Digite a seu endereço: '))
                while True: #loop
                    print(f'{nome}, está correto?') #pergunta aou usuário se ele digitou o nome Certo
                    resposta = input() #pede uma resposta
                    if(resposta in positivo): #vê se a resposta está na lista (positivo)
                        break
                    elif(resposta in negativo): #vê se a resposta está na lista (negativo)
                        print('Certo, Digite novamente.')
                        nome = input ('Digite seu nome: ') #pede para o usuário corrigir o nome
                        print(nome)
                while True:
                    print(f'{email}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, Digite novamente.')
                        email = input ('Digite seu e-mail: ')
                        print(email)
                while True:
                    print(f'{telefone}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, Digite novamente.')
                        telefone = int(input('Digite seu telefone: '))
                        print(telefone)
                while True:
                    print(f'{endereço}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, Digite novamente.')
                        endereço = int(input('Digite seu endereço: '))
                        print(endereço)
                print('Cadastro finalizado')
            elif(resposta == 3):
                nome = input ('Digite seu nome: ') #entrada de dados
                email = input('Digite seu email: ') #entrada de dados
                senha = input('Digite uma senha forte: ')
                telefone = int(input('Digite seu telefone: ')) #entrada de dados de números inteiros
                endereço = int(input('Digite o seu endereço: '))
                while True: #loop
                    print(f'{nome}, está correto?') #pergunta aou usuário se ele digitou o nome Certo
                    resposta = input() #pede uma resposta
                    if(resposta in positivo): #vê se a resposta está na lista (positivo)
                        break
                    elif(resposta in negativo): #vê se a resposta está na lista (negativo)
                        print('Certo, digite novamente.')
                        nome = input ('Digite seu nome: ') #pede para o usuário corrigir o nome
                        print(nome)
                while True:
                    print(f'{email}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, digite novamente.')
                        email = input ('Digite seu email: ')
                        print(email)
                while True:
                    print(f'{telefone}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, digite novamente.')
                        telefone = int(input('Digite seu telefone: '))
                        print(telefone)
                while True:
                    print(f'{endereço}, está correto?')
                    resposta = input()
                    if(resposta in positivo):
                        break
                    elif(resposta in negativo):
                        print('Certo, digite novamente.')
                        endereço = int(input('Digite seu endereço: '))
                        print(endereço)
                print('Cadastro finalizado.')
        elif (escolha == 3): #verifica se o que usuário digitou é igual a 3
            idade = int(input('Digite sua idade: ')) #pergunta para o usuário
            sexo = input('Digite seu sexo: ') #pertunta para o usuário
            controleMasc = ['homem','macho','masculino','m','menino'] #cria uma lista para multiplas respostas do usuário
            controleFem = ['mulher','menina','femia','feminino','f'] #cria uma lista para multiplas respostas do usuário
            if (idade <= 17): #verifica se o que usuário digitou é igual ou menor a 17
                 print('Você atende aos requerimentos.')
            elif (sexo in controleFem): #verifica se o que usuário digitou esta dentro do controleFem
                print('Você atende aos requerimentos.')
            elif (idade > 17 and sexo in controleFem): #verifica se o que usuário digitou é maior que 17 e se esta dentro do controleFem
                 print('Você atende aos requerimentos.')
            else:
                print('Você não atende aos requerimentos.')
        elif(escolha == 4):
            print('Você já possui cadastro?')
            resposta = input()
            if (resposta in positivo):
                    input('Digite seu email:')
                    input('Digite sua senha:')
                    print('ok, um momento.')
            else:
                print('Por favor, realize seu cadastro.')

        elif(escolha == 5):
            while True:
                print('Digite o dia, o mês e a hora que você quer agendar a sua consulta.')
                dia = int(input('dia: '))
                mes = int(input('mês: '))
                hora = float(input('hora: '))
                if(0 < dia <= 31 and 0 < mes <= 12 and 7 <= hora <= 19):
                    print('Agendado!')
                    break
                else:
                    print('Algo deu errado,tente novamente.')
        else:
            break
    else:
        print('Perdão poderia repetir?\n')
        