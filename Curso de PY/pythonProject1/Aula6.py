# #Organizando conjuntos e subconjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {13, 45, 32, 23, 6}
juncao = conjunto.union(conjunto2)#juntar dados
print("União: {} " .format(juncao))

interseccao = conjunto.intersection(conjunto2)
print("intersecção: {}" .format(conjunto))

#Diferença entre um e outro
diferenca = conjunto.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto)
print("Diferença entre 2 e 1: {} ".format(diferenca2))
print("Diferença entre 1 e 2: {} ".format(diferenca))

#Diferença simétrica
dif_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferença simétrica: {}" .format(dif_simetrica))


#Verifica se um conjunto é um subconjunto de outro (subset), contendo todos os produtos que tenham no outro.
conjunto_a = {1,2,3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print("A é um subconjunto de B: {}".format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print("B é um subconjunto de A: {}" .format(conjunto_subset))

#Remover duplicidade de uma lista
Pets = ["Alice", "Shen", "Cookie", "Petit", "Kittie", "Alice"]
conj_pets = set(Pets)#Modo de conjunto
print(conj_pets)
Pets.sort()
Pets = list(Pets)#Modo lista
print(Pets)
Pets = set(Pets)
print(sorted(Pets))

# conjunto = {1, 2, 3, 4}
# conjunto.add(9)
# conjunto.discard(3)
# print(conjunto)
#
