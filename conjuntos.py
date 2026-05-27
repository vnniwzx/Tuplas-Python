#Criando um conjunto chamado "jogos" (É usado chaves para criar um conjunto)
jogos = {'Valorant', 'Fortnite', 'Roblox'}

#Conjuntos não tem posição (Não é possível exibir um elemento pelo número)
print(jogos)

#Adicionando "Minecraft" aos conjuntos
jogos.add('Minecraft')
print(jogos)

#Percorrendo o conjunto e exibindo
for jogo in jogos:
    print(jogo)

#Removendo "Fortnite" dos conjuntos
jogos.remove('Fortnite')
print(jogos)

#Adicionando "Valorant" aos conjuntos (Não dá erro apesar de já existir)
jogos.add('Valorant')
print(jogos)

#Verificando se existe o item em conjuntos
jogo = input("Digite o nome do jogo: ")

if 'Valorant' in jogos:
    print('Este jogo já existe em conjuntos')
else:
    print('Não existe este jogo em conjuntos')
