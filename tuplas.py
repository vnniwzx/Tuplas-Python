#Criando a Tupla chamada "jogos" (É usado colchetes para criar uma tupla)
jogos = ('Valorant', 'Fortnite', 'Roblox')

#Exibe o valor "Fortnite" da tupla
print(jogos[1])

#Percorrendo a tupla
for jogo in jogos:
    print(jogo)

#Tamanho da tupla
print(len(jogos))

#Adicionando itens a tupla (Este comando gera erro pois tupla é imutável)
jogos.append('Minecraft')

#Alterar um elemento da tupla (Este comando gera erro pois tupla é imutável)
jogos[1] = 'Tibia'
