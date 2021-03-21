

class Animale:
    def __init__(self, nome, eta, sesso):
        self.nome = nome
        self.eta = eta
        self.sesso = sesso

    def mangia(self):
        pass


class Cane(Animale):
    def parla(self):
        print("bau")


class Gatto(Animale):
    def parla(self):
        print("Miao")


class Topo(Animale):
    def parla(self):
        print("Squit")


cane = Cane("Mario", 5, "M")
gatto = Gatto("Felix", 3, "M")
topo = Topo("Gigio", 1, "M")




