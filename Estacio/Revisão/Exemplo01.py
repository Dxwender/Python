#VARIAVEIS
#nome_carta      = 'Advgado Constituido'
#classe_carta    ='Druida'
#custo_mana      =2
#pontos_ataque   =1
#pontos_vida     =3
#colecionavel    =True
#eperacoes
#total_mana=10
#subrtracao
#custo_mana=2
#total_mana=total_mana-custo_mana
#imprmir
#print(total_mana)
#entrada/saida dados
#entrada
#nome_carta=input('Qual o nome da carta')
#pontos_vida=int(input('Quantos pontos de vida'))
#verificar conversao
#print(type(nome_carta))
#print(type(pontos_vida))
#saida
#print(nome_carta)
#print(pontos_vida)
#ESTRUTURA CONDICAO
#mana_jogador=5
#mana_invocar=int(input('Custo de mana do card:'))
#if mana_jogador > mana_invocar:
#    print("A carta foi posicionada na a mesa")
#LISTA
pokedex=['Bulba','Charm','Squirt','Butter','Pikachu']
#Ver tamanholista
#print(len(pokedex))
#Acesso de elemetos
#pos=3
#print(f"{pokedex[pos]} escolho vc")
#Acesso partes lista
#print(pokedex[1:4])
#Acesso ulto item
#print(pokedex[-1])
#Add lista
#card_deck=[]
#card_deck.append('Pica')
#card_deck.append('char')
#print(card_deck)
#Estrutura de repticao
#For
#pokedex=[]
#for pokemon in pokedex:
#    print(f"{pokemon} esta na sua pokedex")
#else:
#    print("Esse e o final da  lista")
#While
#print("Nova lista")
#inserir='1'
#novo_deck=[]

#while inserir=='1':
#    novo_card =input('Qual e o seu novo pokemon')
#    novo_deck.append(novo_card)
#    inserir=input('Desesja inseriric cara novamento? (1)sim (2)nao ')
#print(f"Seu novo deck tem {len(novo_deck)} cards")
#Funcoes
#Criar funcoes
novo_deck=[]
#inserir
def inserir_novo():
    novo=input('Qual o nome do pokemon')
    #novo_deck.append(novo)
    if verificar(novo):
        novo_deck.append(novo)
    else:
        print('Ja existe')


#consusltar

#verificar
def verificar (pokemon):
    if pokemon in novo_deck:
        return False
    else:
        return True

#Invocar
inserir_novo()
inserir_novo()