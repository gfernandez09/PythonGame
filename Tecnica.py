class Tecnica:
    def __init__(self, Nombre, Daño, Contador):
        self.Nombre = Nombre
        self.Daño = Daño
        self.Contador = Contador

    def __str__(self):
        return self.Nombre + ", " + str(self.Daño) + ", " + str(self.Contador)