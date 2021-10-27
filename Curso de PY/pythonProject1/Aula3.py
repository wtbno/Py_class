primeira_nota = int(input("Insira sua primeira nota: "))
while primeira_nota > 10:
        primeira_nota = int(input("Nota inserida incorreta, entre com uma nota válida: "))

segunda_nota = int(input("Insira sua segunda nota: "))
while primeira_nota > 10:
        segunda_nota = int(input("Nota inserida incorreta, entre com uma nota válida: "))
terceira_nota = int(input("Insira sua terceira nota: "))
while primeira_nota > 10:
        terceira_nota = int(input("Nota inserida incorreta, entre com uma nota válida: "))
quarta_nota = int(input("Insira sua quarta nota: "))
while primeira_nota > 10:
       quarta_nota = int(input("Nota inserida incorreta, entre com uma nota válida: "))
nota_final = primeira_nota + segunda_nota + terceira_nota + quarta_nota / 4
print("Sua média é:  " + format(nota_final))









# a = int(input("Entre com o primeiro número: "))
# b = int (input("Entre com o segundo valor: "))
#
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0: #uso de operador lógico or e not, inverte a condição de V para F
#     print("foi digitado um número par")
# else:
#     print("nenhum número par foi digitado")



# if resto == 0:
#     print("O número é par " )
# else:
#     print("O número é ímpar ")



#Condicionais
# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))
# if a > b and a > c:
#     print("O maior número é: {}" .format(a))
# elif b > a and b > c:
#     print("O maior número é: {}" .format(b))
# else:
#     print("O maior número é: {}" .format(c))
# print("Final do programa")