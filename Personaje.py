class Personaje:
    def __init__(self, Nom, Tipus, Atac, Vida,Escudo):
        self.Nom = Nom
        self.Tipus = Tipus
        self.Atac = Atac
        self.Vida = Vida
        self.Escudo = Escudo
        self.Tecnicas = []

    def rellenarArray(self, Tecnica):
        self.Tecnicas.append(Tecnica)

    def __str__(self):
        mostrarP = self.Nom + "," + self.Tipus + "," + self.Atac + "," + self.Vida + "," + self.Tecnicas
        return mostrarP
