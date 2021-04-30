class Personaje:

    def __int__(self):
        pass

    def __init__(self, nom, tipus, atac, vida, escudo, tecnica1, tecnica2, tecnica3):
        self.nom = nom
        self.tipus = tipus
        self.atac = atac
        self.vida = vida
        self.escudo = escudo
        self.tecnicas = [tecnica1, tecnica2, tecnica3]

    # Llenamos la lista tecnica
    def rellenarArray(self, Tecnica):
        self.tecnicas.append(Tecnica)

    # Método para listar los detalles del personaje junto con sus tecnicas
    def detalles(self):
        return "Tipo: " + self.tipus + "\nAtaque: " + str(self.atac) + "\nVida: " + str(self.vida) + "\nTecnicas{\n\t["
        + str(self.tecnicas[0]) + "]\n\t[" + str(self.tecnicas[1]) + "]\n\t[" + str(self.tecnicas[2]) + "]\n}"

    #Getters & Setters
    def getNom(self):
        return self.nom

    def getTipus(self):
        return self.tipus

    def getAtac(self):
        return self.atac

    def getVida(self):
        return self.vida

    def getEscudo(self):
        return self.escudo

    def getTecnica(self, num):
        return self.tecnicas[num - 1]

    def setNom(self, nom):
        self.nom = nom

    def setTipus(self, tipus):
        self.tipus = tipus

    def setAtac(self, atac):
        self.atac = atac

    def setVida(self, vida):
        self.vida = vida

    def setEscudo(self, escudo):
        self.escudo = escudo

    def __str__(self):
        return self.nom
