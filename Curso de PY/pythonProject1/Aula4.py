#Laços de repetição
#while fazer uma repetição até que seja verdadeiro
nota = int (input("Entre com uma nota:"))
while nota > 10:
    nota = int(input("Nota inválida, entre com a nota correta: "))
a = 0
while a <= 10:
    print(a)
    a += 1






# a = int (input("Entre com um valor"))
# for num in range (101):
#     div = 0
#     for x in range (1, num+1):#for dentro de for
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

















# a = int(input("Insira um número: "))
# div = 0
# for x in range (1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
#
# if div == 2:
#     print("Número {} é primo" .format(a))
# else:
#     print("Número {} não é primo" .format(a))
# for x in range(1, 500):
#     print(x)