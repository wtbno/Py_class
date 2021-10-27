class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def aum_canal(self):
        if self.ligada:
            self.canal += 1
    def dim_canal(self):
        if self.ligada:
            self.canal -=1




televisao = TV ()
print("A TV está ligada: {}".format(televisao.ligada))
televisao.power()
print("A TV está ligada: {}".format(televisao.ligada))
televisao.power()
print("A TV está ligada: {}".format(televisao.ligada))
print("Canal: {}" .format(televisao.canal))
televisao.power()
televisao.aum_canal()
televisao.aum_canal()
print("Canal: {}".format(televisao.canal))
televisao.dim_canal()
print("Canal: {}". format(televisao.canal))