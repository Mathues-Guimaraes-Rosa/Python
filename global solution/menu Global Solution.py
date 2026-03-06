import re
import random

controle = [1, 2, 3, 4, 5, 6, 7, 8] #lista para controle
positivo = ['sim','s','ss','sss','si'] #lista para controle
logado = False #guarda se o usuário está ou não logado
usuario_logado = None #guarda o usuário qual está logado
usuario = {} #dicionário para guardar informações de usuarios

def empregos(escolha): #criando uma função para reutilização futura do codigo
    if (escolha == 1):
        print("""\nEmpregos:

    - Técnico ou engenheiro em energia solar/fotovoltaica

    - Técnico em energia eólica

    - Especialista em eficiência energética

    - Instalador de painéis solares

    - Analista de sustentabilidade energética

    - Gestor de projetos em bioenergia (etanol, biogás, biodiesel)\n""")
        
    elif(escolha == 2):
        print("""\nEmpregos:

    - Engenheiro agrônomo sustentável

    - Técnico em agroecologia

    - Consultor em agricultura regenerativa

    - Especialista em compostagem e manejo de resíduos orgânicos

    - Pesquisador em bioinsumos e controle biológico\n""")
        
    elif(escolha == 3):
        print("""\nEmpregos:

    - Analista de sustentabilidade

    - Gestor ambiental

    - Consultor em licenciamento ambiental

    - Perito em impacto ambiental

    - Especialista em ESG (Environmental, Social and Governance)

    - Auditor ambiental\n""")
        
    elif(escolha == 4):
        print("""\nEmpregos:

    - Arquiteto sustentável / urbanista verde

    - Engenheiro civil especializado em construções sustentáveis

    - Especialista em mobilidade urbana elétrica

    - Designer de paisagens ecológicas

    - Planejador de cidades resilientes\n""")
        
    elif(escolha == 5):
        print("""\nEmpregos:

    - Gestor de resíduos sólidos

    - Engenheiro de reciclagem e reaproveitamento

    - Analista de economia circular

    - Coordenador de logística reversa

    - Empreendedor social de reaproveitamento de materiais\n""")
    elif(escolha == 6):
        print("""\nEmpregos:

    - Desenvolvedor de soluções de eficiência energética (IoT verde)

    - Especialista em data centers sustentáveis

    - Analista de pegada de carbono digital

    - Gestor de TI com foco em sustentabilidade

    - Engenheiro de blockchain para rastreabilidade ecológica\n""")
        
    elif(escolha == 7):
        print("""\nEmpregos:

    - Educador ambiental

    - Pesquisador em sustentabilidade

    - Instrutor em práticas ecológicas

    - Coordenador de projetos socioambientais

    - Gestor de impacto social\n""")
    else:
        print('Por favor, digite uma opção válida.')

def mostrar(numero, nome, id): #criando uma função para reutilização futura do codigo
    if (numero == 1):
        print("""| Nº | Data       | Atividade                                   | Descrição                                                      | ImpactCoins |
| -- | ---------- | ------------------------------------------- | -------------------------------------------------------------- | ----------- |
| 1  | 10/10/2025 | Cadastro no Green                           | Criação do perfil sustentável (Green ID)                       | +5          |
| 2  | 11/10/2025 | Curso: Fundamentos da Economia Verde        | Conclusão do módulo introdutório (IA Gaia)                     | +10         |
| 3  | 12/10/2025 | Ação Comunitária: Limpeza Urbana            | Participou de mutirão local organizado pelo GreenHub São Paulo | +15         |
| 4  | 14/10/2025 | Projeto: “Refloresta 2050”                  | Plantio de 10 mudas nativas em área degradada                  | +10         |
| 5  | 15/10/2025 | Curso: Sustentabilidade Digital             | Certificação registrada em blockchain                          | +10         |
| 6  | 17/10/2025 | Voluntariado Online                         | Mentoria para jovens sobre profissões verdes                   | +10         |
| 7  | 19/10/2025 | Evento: Fórum Verde Local                   | Participou de palestra sobre transição energética              | +5          |
| 8  | 21/10/2025 | Trilha de Aprendizado Verde — IA Gaia       | Conclusão de 3 trilhas personalizadas                          | +15         |
| 9  | 22/10/2025 | Projeto de Reciclagem “ReUse+”              | Entrega de 15 kg de resíduos recicláveis                       | +10         |
| 10 | 25/10/2025 | Feedback e Engajamento na Comunidade        | Contribuição em discussões de GreenHub                         | +5          |
| 11 | 26/10/2025 | Curso: Introdução ao Blockchain Sustentável | Certificação emitida via Green ID                              | +10         |
| 12 | 28/10/2025 | Doação Ecológica                            | Doou 20 ImpactCoins a projeto de energia solar comunitária     | −20         |
| 13 | 30/10/2025 | Projeto “Cidades Verdes”                    | Desenvolvimento de proposta de mobilidade elétrica             | +15         |
| 14 | 01/11/2025 | Recompensa de Impacto Mensal                | Bônus por engajamento positivo e ações contínuas               | +10         |
    """)
    elif (numero == 2):
        print("""\nOpções proxima a você:
1 - Comunidade de Energia Solar - São Paulo
2 - Projeto Refloresta
3 - ReciclaTech - Economia Circular\n""")
    elif(numero == 3):
        print(f"""\nUsuário: {nome}
Green ID: {id}
Nível de Engajamento:  Agente Verde Ativo
Período Avaliado: 10/10/2025 – 01/11/2025
Saldo Atual: 120 ImpactCoins

    Resumo Geral:
| Indicador                    | Resultado                    | Descrição                                                    |
| ---------------------------- | ---------------------------- | ------------------------------------------------------------ |
| 🌎 Impacto Total             | **140 ImpactCoins gerados**  | Representa o total de ações sustentáveis realizadas.         |
| ♻️ Ações Realizadas           | **13 atividades concluídas** | Cursos, projetos e voluntariado.                             |
| 📚 Trilhas de Aprendizado    | **3 trilhas concluídas**     | Economia Verde, Sustentabilidade Digital e Blockchain Ético. |
| 👥 Projetos Comunitários     | **2 GreenHubs ativos**       | Refloresta 2050 e ReUse+.                                    |
| 💧 CO₂ Compensado (estimado) | **≈ 85 kg**                  | Equivalente a plantar 5 árvores nativas.                     |
| 💡 Horas de Engajamento      | **≈ 42 h**                   | Tempo dedicado a atividades de impacto.                      |

    Detalhamento de Ações:
| Tipo de Ação                      | Quantidade | ImpactCoins                   |
| --------------------------------- | ---------- | ----------------------------- |
| Cursos e Trilhas Educacionais     | 4          | +40                           |
| Voluntariado e Comunidade         | 3          | +30                           |
| Projetos de Sustentabilidade      | 3          | +35                           |
| Participação em Eventos / Fórum   | 1          | +5                            |
| Contribuições Digitais / Mentoria | 2          | +10                           |
| Doações Ecológicas                | 1          | −20                           |
| **Total**                         | **14**     | **120 ImpactCoins (líquido)** |

    ODS Contribuídos:

As ações deste usuário contribuíram diretamente com os seguintes Objetivos de Desenvolvimento Sustentável (ONU):

| ODS   | Objetivo                                 | Contribuição                                         |
| ----- | ---------------------------------------- | ---------------------------------------------------- |
| 🟦 4  | Educação de Qualidade                    | Participação em trilhas verdes e mentoria ambiental. |
| 🟩 8  | Trabalho Decente e Crescimento Econômico | Apoio a empregos verdes e startups sustentáveis.     |
| 🟧 10 | Redução das Desigualdades                | Inclusão de jovens em projetos comunitários.         |
| 🟥 13 | Ação contra a Mudança Global do Clima    | Redução de CO₂ via reflorestamento e reciclagem.     |


    Progresso de Carreira Verde:

Trilha Atual: “Transição Energética e Cidades Sustentáveis”

Próxima Recomendação da IA Gaia: “Economia Circular e Design Regenerativo”

Certificações Blockchain Ativas:

Sustentabilidade Digital (emitida em 15/10/2025)

Blockchain Ético (emitida em 26/10/2025)

    Avaliação da IA Gaia:

“O usuário demonstra alta coerência entre propósito e ação.
Recomendado para liderança de projetos GreenHub e mentorias em educação ambiental.”

    Índice de Impacto Global (IIG):

Pontuação Atual: 78/100
Posição no Ranking Regional: Top 12% (GreenHub Brasil)

    Recompensa:

Você recebeu o selo:
“Agente Regenerativo 2025” — concedido a usuários que ultrapassam 100 ImpactCoins em ações verificadas.

    Mensagem Final:

“Cada ação verde é um código que reprograma o futuro do planeta.
Continue evoluindo sua jornada com propósito — o mundo precisa do seu impacto.”

— Equipe Green / IA Gaia\n""")

def gerarIDUnico(): #criando uma função para reutilização futura do codigo
    while True:
        novo_id = random.randint(1, 100000000000) #gera um número aleatório
        
        if (not any(dados["ID"] == novo_id for dados in usuario.values())): # verifica se o ID já existe
            return novo_id
        
def confirmarCadastro(email, senha, areaInteresse, experiencia, nome, id): #criando uma função para reutilização futura do codigo
    verificacao = input("As informações estão corretas? ").lower()
    if (verificacao in positivo):
        
        print(f'seu id é {id}')
        print('Cadastro finalizado. \n')
        
        usuario[email] = { #cria um sub-dicionario para guardar informações de usuarios
        "nome": nome,
        "senha": senha,
        "área de interesse": areaInteresse,
        "nível de experiência": experiencia,
        "ID" : id
    }
        return(True)
    else:
        print('Digite as informações novamente.')
        return(False)

print('    ------ Bem vindo ao Green Team ------ \n')

while True: #inicia um loop infinito (ter cuidado para não ficar em um loop infinito, sempre ter uma rota de escape)
    print('Escolha uma das opções abaixo: \n')
    print('1 - Criar Green ID.') #imprime na tela um texto
    print('2 - Entrar / Login.') #imprime na tela um texto
    print('3 - Explorar Empregos Verdes.') #imprime na tela um texto
    print('4 - Trilhar Aprendizado Verde (IA Gaia).') #imprime na tela um texto
    print('5 - Carteira ImpactCoin.') #imprime na tela um texto
    print('6 - Projetos e Comunidades (GreenHubs).') #imprime na tela um texto
    print('7 - Relatórios de Impacto.') #imprime na tela um texto
    print('8 - Sair.') #imprime na tela um texto

    try:
        escolha_menu = int(input('Digite a opção desejada: ')) #pede para o usuário digitar um número inteiro
        if (escolha_menu in controle): #verifica se o que o usuário digitou está dentro da lista
            if(escolha_menu == 1): #verifica se o que o usuário digitou é igual a 1
                while True:
                    nome = input('Digite seu nome: ').lower() #entrada de dados
                    areaInteresse = input('Digite sua área de interesse: ')
                    experiencia = input('Digite seu nível de experiência: ')
                    email = input('Digite seu e-mail: ').strip().lower() #entrada de dados
                    if (not re.search(r'[\w\.-]+@[\w\.-]+\.\w+', email)):
                        print('E-mail inválido.')
                    else:   
                        senha = input('Digite uma senha forte: ') #entrada de dados
                        senhaRedigitada = input('Redigite sua senha: ') #entrada de dados
                        if (senha != senhaRedigitada):
                            print('Erro: as senhas devem ser iguais \n')
                        else:
                            id = gerarIDUnico()
                            print('\n' + nome)
                            print(email)
                            print(areaInteresse)
                            print(experiencia , '\n')
                            if(confirmarCadastro(email, senha, areaInteresse, experiencia, nome, id) == True):
                                break
            elif(escolha_menu == 2): #verifica se o que o usuário digitou é igual a 2 
                email_digitado = input('Digite seu e-mail: ')
                senha_digitada = input('Digite sua senha: ')
                
                if (email_digitado in usuario and usuario[email_digitado]["senha"] == senha_digitada):
                    print(f"Login bem-sucedido! Bem-vindo, {usuario[email_digitado]['nome'].title()}.\n")
                    logado = True
                    usuario_logado = email_digitado
                else:
                    print('Email ou senha incorretos.\n')    
            elif (escolha_menu == 3): #verifica se o que o usuário digitou é igual a 3
                print('\n1 - Energias Renováveis.')
                print('2 - Agricultura Sustentável e Agroecologia.')
                print('3 - Gestão Ambiental e Consultoria Ecológica.')
                print('4 - Cidades Inteligentes e Infraestrutura Verde.')
                print('5 - Economia Circular e Gestão de Resíduos.')
                print('6 - Tecnologia Verde e Sustentabilidade Digital.')
                print('7 - Educação, Pesquisa e Impacto Social.')
                try:
                    escolha_empregos = int(input('Digite a opção desejada: '))   
                    empregos(escolha_empregos) 
                except ValueError:
                    print('Por favor, digite um número. \n')
            elif(escolha_menu == 4):
                if (logado == True): 
                    print("""Com base no seu perfil, recomendamos:
                        → Curso: Fundamentos da Economia Verde
                        → Trilha: Transição Energética e Cidades Sustentáveis """)
                else:
                    print('\nPor favor, realize seu login.\n')
            elif(escolha_menu == 5):
                if(logado == True):
                    print('\nSeu saldo: 120 ImpactCoins:')
                    print('1 - Trocar por dinheiro ou cursos.')
                    print('2 - Doar a um projeto verde.')
                    print('3 - Ver histórico de transações.')
                    try:
                        escolha_ImpactCoins = int(input('Digite a opção desejada:  '))                       
                        if(escolha_ImpactCoins == 1):
                            print('Você pode trocar suas ImpactCoins por 1,20 R$ ou por 1 curso(s).')
                            print('1 - Para 1,20 R$')
                            print('2 - Para 1 curso(s)')
                            try:
                                escolha_troca = int(input('Digite a opção desejada: '))
                                if(escolha_troca == 1):
                                    print('Valor transferido para a sua conta.')
                                elif(escolha_troca== 2):
                                    print('O curso estará disponível em breve.')
                                else:
                                    print('Digite uma opção válida.')
                            except ValueError:
                                print('Por favor, digite um número.')
                        elif(escolha_ImpactCoins == 2):
                            print('Obrigado por colaborar conosco para manter o planeta saudável.')
                        elif(escolha_ImpactCoins == 3):
                            mostrar(1, None , None)
                    except ValueError:
                        print('Por favor, digite um número.')
                else:
                    print('Por favor, realize seu login.')
            elif(escolha_menu== 6):
                mostrar(2, None, None)
            elif(escolha_menu == 7):
                if(logado == True):
                    mostrar(3,usuario[usuario_logado]["nome"].capitalize(), usuario[usuario_logado]["ID"] )
                else:
                    print('Por favor, realize seu login.')
            elif(escolha_menu == 8):
                logado = False
                usuario_logado = None
                break
        else:
            print('\nPor favor, digite uma opção válida! \n')
    except ValueError:
        print('\nPor favor, digite um número. \n')
        