meu_dicionario = {
'tecnologia_1' : {"codigo" : 1 , "linguagem" : 'Python'}, 
'tecnologia_2' : {"codigo" : 2 , 'linguagem' : 'Java'}, 
'tecnologia_3' : {'codigo' : 3 , 'linguagem' : 'PHP'}
}
print(meu_dicionario)
print(type(meu_dicionario))
for tecnologia in meu_dicionario.values():
    print(tecnologia['linguagem'])
print(len(meu_dicionario))


dicionario_frutas = {
'chave_1': {'nome':'limao','tipo':'ácida'},
'chave_2': {'nome':'laranja','tipo': 'ácida'},
'chave_3': {'nome': 'manga','tipo':'semiácida'},
'chave_4': {'nome': 'maça','tipo':'semiácida'},
'chave_5': {'nome': 'banana','tipo':'doce'},
'chave_6': {'nome': 'mamão','tipo':'doce'}
}

print(dicionario_frutas['chave_1']['nome'])
print(type(dicionario_frutas['chave_1']))
print(dicionario_frutas['chave_2']['nome'])
print(type(dicionario_frutas['chave_2']))   

for frutas in dicionario_frutas.values():
    print(frutas['nome'],frutas['tipo'])