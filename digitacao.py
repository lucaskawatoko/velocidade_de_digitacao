import datetime
import random

import sqlite3

print("")
print('''sou um programa criado na intenção de ajudar a evoluir sua velocidade de digitação
''')

nome_suario = str(input('informe seu nome ')) # pede o nome do usuario 
contagem = 1
palavras = ['bola','casa','carro','bmw','sol','moto','silva',
            'faca','melancia','tomate','dado','pera','cartão',
            'ano novo','lua','luva','oi','computador','casa',
            'corsa','caneta','teclado','tecla','digito','carregador',
            'câmera','tatu','telha','celular','cama','navio',
            'barro','internet','python','papel','papelão','banana','bolsa',
            'geladeira','volume','peixe','casa','janela','perna','imagens'
            'começo','como','mulher','homem','bom','mal','mau','final','roça',
            'tempo','filtro de ar','gato','cachorro','pai','mãe','dente','dentadura'
            'rapadura','camelo','fox','terminal','termino','agora','depois','cheiro',
            'larva','larissa','camila','eduardo','duda','ricardo','adriana','daniela',
            'máximo','mínimo','ocupado','palha','palhaço','bateria','luz','acesso','aceso',
            'apagado','apagão','ranking','gol','desenho','desenhar','cachaça','pausa'] # lista de palvras para o programa sortear e pedir para o usuario escrever

escolha = random.choice(palavras) # escolha da palavra
print(f'vc tem que digita a palavra {escolha}')
comeco = datetime.datetime.now() # começo do contagem de tempo da digitação do usuario
tentativa = str(input('digite aqui a palavra escolhida')) # campo para o usuario digitar a palavra
while True:
    if tentativa != escolha:
        print(f'vc digitou a palavra {tentativa} e não a palavra {escolha}')
        print('tente novamente')
        contagem += 1
        tentativa = str(input('digite aqui a palavra escolhida'))
    elif tentativa == escolha:
        print(f'parabens {nome_suario} vc digitou a palavra de forma correta com {contagem} tentativas')
        break

# loop para o usuario tentar escrever a palavra (loop,contagem,tempo só vai para quando o usuario certar a palavra )

final = datetime.datetime.now()
tempo = (final - comeco)
t = str(tempo) # transformando o tempo em string (texto)
print(f"seu tempo foi {tempo}")

banco = sqlite3.connect("ranking.db") # criando o banco de dados com o nome ranking.db

cursor = banco.cursor() # conectando ao banco 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ranking_de_digitacao(
        Nome TEXT NOT NULL,
        Palavra TEXT NOT NULL,
        Tentativa TEXT NOT NULL,
        Tempo TEXT NOT NULL
);
''') # criando a tabela no banco com  o Ranking_de_digitacao
cursor.execute('''
    INSERT INTO Ranking_de_digitacao(Nome,Palavra,Tentativa,Tempo)VALUES(?,?,?,?)
''',(nome_suario,escolha,contagem,t)) # inserindo as informações na tabela 

banco.commit() # finalizando a conexão do banco
