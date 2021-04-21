class Personaje:
    def __init__(self, Nom, Tipus, Atac, Vida, Escudo, Tecnica1, Tecnica2, Tecnica3):
        self.Nom = Nom
        self.Tipus = Tipus
        self.Atac = Atac
        self.Vida = Vida
        self.Escudo = Escudo
        self.Tecnicas = [Tecnica1, Tecnica2, Tecnica3]

    def rellenarArray(self, Tecnica):
        self.Tecnicas.append(Tecnica)

    def detalles(self):
        return "Tipo: " + self.Tipus + "\nAtaque: " + str(self.Atac) + \
               "\nVida: " + str(self.Vida) + "\nTecnicas{\n\t[" + \
               str(self.Tecnicas[0]) + "]\n\t[" + str(self.Tecnicas[1]) + \
               "]\n\t[" + str(self.Tecnicas[2]) + "]\n}"

    def __str__(self):
        return "Nombre: " + self.Nom