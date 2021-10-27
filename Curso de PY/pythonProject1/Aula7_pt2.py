#Métodos, funções e classes
#Função é tudo que retorna um valor
#Método não retorna um valor (é chamado definição em py (def)), os métodos aux. para não ficar regerando cod.
#Para converter um método em uma classe, se utiliza Class + um nome desejado com caixa alta.
#REFATORAÇÃO
class Calculadora:
    def __init__(self):#nesse caso o init não pode ser vazio
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    # A partir disso, é possível chamar o método de fora

    def subst(self, valor_a, valor_b):
        return valor_a - valor_b


    def div (self, valor_a, valor_b):
        return valor_a / valor_b


    def mult (self,valor_a, valor_b):
        return valor_a * valor_b

calculadora = Calculadora(50, 3)
print(calculadora.valor_a)
print(calculadora.valor_b)
print(calculadora.soma())
print(calculadora.subst())
print(calculadora.mult())
print(calculadora.div())


