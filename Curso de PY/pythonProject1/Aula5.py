#Como organizar os dados em uma lista ou tupla e realizar operações
lista = [1, 7, 8, 9,]
print(lista)
lista_animal = ["Shen", "Cookie", "Kittie"]
print(lista_animal [2])#forma de acessar um determinado dado especifico dentro da lista com []
print(type(lista_animal))
for x in lista_animal:
    print(x)


soma = 0 #forma de reações dentro da lista
for y in lista:
    print(y)
    soma += y
print(soma)

print(sum(lista)) #forma simplificada de soma de dados dentro de uma lista
print(max(lista))
print(min(lista))


if "Petit" in lista_animal:
    print("Existe a Petit na lista")
else:
    print("Não existe a Petit na lista")
    lista_animal.append("Petit")#Inclusão de um dado na lista caso ele não exista
    print(lista_animal)

lista_animal.pop()#retira o último animal da lista, ou o dado solicitado em ()
print(lista_animal)

lista_animal.sort()#Ordenação
print(lista_animal)
lista_animal.reverse()#Ordenação reversa

#Tuplas
#Tupla imutável
#Lista mutável
tupla =  (54, 85, 99, 11, 39, 56)
print(tupla)
print(len(tupla))#contador
print(len(lista_animal))
tupla_animal = tuple (lista_animal)#conversão
print(tupla_animal)