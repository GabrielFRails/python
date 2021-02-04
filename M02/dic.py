#dicionários
estudantes = {"Matheus": 24, "Fernanda": 22, "Tamires": 26, "Cristiano": 25}
print(estudantes)

estudantes["Pedro"] = 23
print(estudantes)

idade = estudantes["Pedro"]
print(idade)

print(len(estudantes))

print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())

estudantes2 = {"Maria": 18, "João": 18, "Gabriel": 20}
estudantes.update(estudantes2)
print(estudantes)

dict3 = {'key1':1230,'key2':[22,453,73.4],'key3':['leite','maça','batata']}
print(dict3)

print(dict3['key3'][1].upper())

var = dict3['key2'][0] - 2
print(var)
