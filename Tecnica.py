class Tecnica:
    def __init__(self, nombre, dano, contador):
        self.nombre = nombre
        self.dano = dano
        self.contador = contador

    # Getters & Setters
    def getNombre(self):
        return self.nombre

    def getDano(self):
        return self.dano

    def getContador(self):
        return self.contador

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDano(self, dano):
        self.dano = dano

    def setContador(self, contador):
        self.contador = contador

    def __str__(self):
        return self.nombre + ", " + str(self.dano)
