A = int(input("Entre com o primeiro valor: "))#Interação c/ usuário, onde solicita um dado
B = int(input("Entre com o segundo valor: "))#Ao adicionar o int antes do input, é realizado a conversão
#A = 988
#B = 1485
soma = A + B
divisao = A / B
multiplicacao = A * B
subtracao = A - B
resto = A % B
print("O resultado da soma é: {soma}. "
      "\n Subtração: {subtracao}. "
      "\n Multiplicação: {multiplicacao}. "
      "\n Divisão: {divisao}. "
      "\n resto: {resto}. "
      .format(soma=soma,
              subtracao=subtracao,
              multiplicacao=multiplicacao,
              divisao=divisao,
              resto=resto)) #forma mais correta, com a utilização do .format
#deixar o resultado em ordem conforme a escrita
#print('O resultado da soma é: ' + soma)
#Se faz necessário o uso de {} para que seja impresso corretamente, ou
# faz o uso de uma declaração no final dentro do format

#print(divisao)
#divisao = ("O resultado da divisão é: " + str(divisao))
#print(int(divisao))#conversão de float p/ int

#multiplicacao = ("O resultado da multiplicação é: " + str(multiplicacao))
#print(multiplicacao)

#subtracao = ("O resultado da subtração é: " + str(subtracao))
#print(subtracao)

#resto = ("O resultado do resto da divisão é: " + str(resto))
#print(resto)



#print(type(soma))
#soma = ('O resultado da soma é: ' + str(soma)) #conversão
#print(soma)

#Não é possível imprimir texto em int, sendo preciso a conversão