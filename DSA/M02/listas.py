#criando uma lista
mercado = ["ovos", "cenoura", "Toddy"]
print(mercado)
lista = [123, 32, "ovos"]
print(lista)
print(lista[0])
lista[1] = "chocolate"
print(lista)

#listas aninhadas -> listas dentro de listas
new_lista = [[1,2,3], [22.3, "chocolate", 10], [3,5,7]]
print(new_lista)
a = new_lista[1]
print(a)
b = a[0]
print(b)

a = new_lista[1][1]
print(a)

lista_total = new_lista[0] + new_lista[2]
print(lista_total)

#operador in
print(5 in lista_total)

nova_lista = []

for item in lista_total:
    nova_lista.append(item)

print(nova_lista)

cidades = ["Goiânia", "Cuiabá", "Floripa"]
cidades.extend(["Salvador", "Londres"])
print(cidades)