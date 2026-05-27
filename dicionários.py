#Criando um dicionário
aluno={
    "Nome":"Raphael Ramalho",
    "Idade": 17,
    "Curso": "Informática"
}

#Exibe o item "Nome" e "Curso" do dicionário "aluno"
print(f'{aluno["Nome"]} - {aluno["Curso"]}')

#Alterar um item do dicionário
aluno["Idade"] = 18
print(aluno)

#Cria o item "cidade" e define como "São paulo" mesmo sem existir
aluno["cidade"] = "São Paulo"
print(aluno)

#Remove um item de dicionários
del aluno["cidade"]
print(aluno)

#Percorrendo o dicionário "aluno"
for chave, valor in aluno.items():
    print(f"{chave} - {valor}")
