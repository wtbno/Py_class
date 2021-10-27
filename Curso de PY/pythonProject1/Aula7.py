#Métodos, funções e classes
#Função é tudo que retorna um valor
#Método não retorna um valor (é chamado definição em py (def)), os métodos aux. para não ficar regerando cod.
#Para converter um método em uma classe, se utiliza Class + um nome desejado com caixa alta.

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    # A partir disso, é possível chamar o método de fora

    def subst(self):
        return self.valor_a - self.valor_b


    def div (self):
        return self.valor_a / self.valor_b


    def mult (self):
        return self.valor_a * self.valor_b

calculadora = Calculadora(50, 3)
print(calculadora.valor_a)
print(calculadora.valor_b)
print(calculadora.soma())
print(calculadora.subst())
print(calculadora.mult())
print(calculadora.div())


