from Personaje import Personaje
from Tecnica import Tecnica
import random
import time
import os


class Juego:
    def __init__(self):
        self.personajes = []
        self.personajeJugador = Personaje
        self.personajeCPU = Personaje
        self.turno = 1
        self.contadorVictoria = 0

    # Creamos los personajes del juego con sus respectivas técnicas individuales
    def CreacionPersonajes(self):
        t1_p1 = Tecnica("Hulk Aplasta", 150, 30)
        t2_p1 = Tecnica("Hulk Furioso", 900, 1)
        t1_p2 = Tecnica("Pegar", 130, 30)
        t2_p2 = Tecnica("Ataque Crítico", 150, 3)
        t1_p3 = Tecnica("Estabilizadores de Vuelo", 150, 30)
        t2_p3 = Tecnica("Concentración Láser", 180, 3)
        t1_p4 = Tecnica("Iron Man Aplasta", 80, 30)
        t2_p4 = Tecnica("Veronica", 120, 3)
        t1_p5 = Tecnica("Lanzatelarañas", 120, 30)
        t2_p5 = Tecnica("El cosquilleo de Peter", 150, 3)
        t1_p6 = Tecnica("Lanzatelarañas", 150, 30)
        t2_p6 = Tecnica("Matanza Instantánea", 190, 3)
        t1_p7 = Tecnica("Lanzamiento del Escudo", 150, 30)
        t2_p7 = Tecnica("Aguantaría todo el dia", 190, 3)
        t1_p8 = Tecnica("Golpe con brazo metálico", 150, 30)
        t2_p8 = Tecnica("Ataque Hydra", 190, 3)
        t1_p9 = Tecnica("Ataque Básico", 180, 30)
        t2_p9 = Tecnica("Gemas del Infinito", 220, 3)
        t1_p10 = Tecnica("Llave de combate", 150, 30)
        t2_p10 = Tecnica("Entrenamiento Natasha", 180, 3)
        t1_p11 = Tecnica("Disparar Flecha", 150, 30)
        t2_p11 = Tecnica("Te he hecho mirar", 180, 3)
        t1_p12 = Tecnica("Ala Roja", 150, 30)
        t2_p12 = Tecnica("Por la Izquierda", 180, 3)
        t1_p13 = Tecnica("Estabilizadores de Vuelo", 150, 30)
        t2_p13 = Tecnica("Concentración Láser", 180, 3)
        escudo = Tecnica("Añadir Escudo", 0, 30)

        personaje1 = Personaje("Hulk", "Tanque", 150, 900, 0, t1_p1, t2_p1, escudo)
        personaje2 = Personaje("Profesor Hulk", "Tanque", 130, 900, 0, t1_p2, t2_p2, escudo)
        personaje3 = Personaje("Iron Man Mark 50", "Versátil", 150, 600, 0, t1_p3, t2_p3, escudo)
        personaje4 = Personaje("Iron Man HulkBuster", "Tanque", 80, 1000, 0, t1_p4, t2_p4, escudo)
        personaje5 = Personaje("Spider-Man", "Versátil", 120, 600, 0, t1_p5, t2_p5, escudo)
        personaje6 = Personaje("Spider-Man Iron Spider", "Versátil", 150, 600, 0, t1_p6, t2_p6, escudo)
        personaje7 = Personaje("Capitan America", "Versátil", 150, 600, 0, t1_p7, t2_p7, escudo)
        personaje8 = Personaje("Lobo Blanco", "Versátil", 150, 600, 0, t1_p8, t2_p8, escudo)
        personaje9 = Personaje("Thanos", "Titán", 180, 900, 0, t1_p9, t2_p9, escudo)
        personaje10 = Personaje("Viuda Negra", "Espia", 120, 450, 0, t1_p10, t2_p10, escudo)
        personaje11 = Personaje("Hawkeye", "Espia", 120, 450, 0, t1_p11, t2_p11, escudo)
        personaje12 = Personaje("Falcon", "Aéreo", 120, 450, 0, t1_p12, t2_p12, escudo)
        personaje13 = Personaje("Maquina de Guerra", "Versátil", 150, 600, 0, t1_p13, t2_p13, escudo)

        # Añadimos los personajes a una lista
        self.personajes = [
            personaje1,
            personaje2,
            personaje3,
            personaje4,
            personaje5,
            personaje6,
            personaje7,
            personaje8,
            personaje9,
            personaje10,
            personaje11,
            personaje12,
            personaje13
        ]

    # Método de Contar las Victorias del jugador
    def setContadorVictoria(self, num):
        self.contadorVictoria = num

    def getContadorVictoria(self):
        return self.contadorVictoria

    # Metodo para listar los personajes y la creación de un ULTRA BOSS
    def listarPersonajes(self):
        if self.contadorVictoria == 5:
            t1_galactus = Tecnica("Destrozo", 500, 30)
            t2_galactus = Tecnica("Comerse el planeta", 1000, 30)
            escudo = Tecnica("Añadir Escudo", 0, 30)
            ultraboss = Personaje("Galactus", "Galactico", 500, 2000, 0, t1_galactus, t2_galactus, escudo)
            self.personajes.append(ultraboss)
            self.contadorVictoria = 0
        print("**Personajes Disponibles**")
        for x in range(0, len(self.personajes)):
            print(self.personajes[x])

    # Método para que el usuario elija un personaje
    def elegirPersonajeJugador(self):
        contador = 0
        salir = True
        personajeElegido = input("Personaje a elegir: ")
        while salir:
            if personajeElegido == self.personajes[contador].getNom():
                self.personajeJugador = self.personajes[contador]
                del self.personajes[contador]
                salir = False

            contador += 1

        print("Jugador elegido por el Usuario: " + str(self.personajeJugador))

    # Método para que la CPU elija un personaje
    def elegirPersonajeCPU(self):
        personajeAleatorio = random.choice(self.personajes)
        self.personajeCPU = personajeAleatorio
        self.personajes.remove(personajeAleatorio)
        print("Jugador elegido por la CPU: " + str(self.personajeCPU))

    # Método para bajar la vida al jugador y a la CPU
    @staticmethod
    def bajarVida(tecnica, personaje):
        if personaje.getEscudo() == 0:
            personaje.setVida(personaje.getVida() - tecnica.getDano())
        else:
            personaje.setEscudo(personaje.getEscudo() - tecnica.getDano())
            if personaje.getEscudo() < 0:
                personaje.setVida(personaje.getVida() - abs(personaje.getEscudo()))
                personaje.setEscudo(0)

    # Turno del Jugador
    def turnoJugador(self):
        self.turno = 2
        print("Comienza el turno del Usuario...")
        time.sleep(3)
        print("Tecnicas del Personaje: " + "\n1.- " + str(self.personajeJugador.getTecnica(1)) + "\n2.- "
              + str(self.personajeJugador.getTecnica(2)) + "\n3.- " + str(self.personajeJugador.getTecnica(3)))
        tecnicaEscogida = int(input("¿Qué tecnica querrías usar? "))
        time.sleep(3)
        self.numRandomJugador = random.choice(range(1, 100))
        if self.numRandomJugador < 90:
            if self.personajeJugador.getTecnica(tecnicaEscogida).getContador() > 0:
                self.bajarVida(self.personajeJugador.getTecnica(tecnicaEscogida), self.personajeCPU)
                if tecnicaEscogida == 3:
                    self.personajeJugador.setEscudo(150)
            else:
                print("Ya no se puede usar mas")
        else:
            print("El personaje " + str(self.personajeCPU.getNom()) + " ha esquivado el ataque")

    # Turno de la CPU
    def turnoCPU(self):
        self.turno = 1
        print("Comienza el turno de la CPU...")
        time.sleep(3)
        print("Tecnicas del Personaje: " + "\n1.- " + str(self.personajeCPU.getTecnica(1)) + "\n2.- "
              + str(self.personajeCPU.getTecnica(2)) + "\n3.- " + str(self.personajeCPU.getTecnica(3)))
        print("Eligiendo con sabiduria :) ...")
        time.sleep(3)
        numRandom = random.choice(range(1, 4))
        time.sleep(3)
        self.numRandomCPU = random.choice(range(1, 100))
        if self.numRandomCPU < 90:
            if self.personajeCPU.getTecnica(numRandom).getContador() > 0:
                self.bajarVida(self.personajeCPU.getTecnica(numRandom), self.personajeJugador)
                if numRandom == 3:
                    self.personajeCPU.setEscudo(150)
            else:
                print("Ya no se puede usar mas")
        else:
            print("El personaje " + str(self.personajeJugador.getNom()) + " ha esquivado el ataque")

    # Bucle para volver a iniciar el juego según el usuario decida si hacerlo o no.
    @staticmethod
    def volverJugar():
        volverJuego = input("¿Deseas volver a jugar? [s/n]")
        if volverJuego == "s":
            return True
        elif volverJuego == "n":
            return False
        else:
            print("Opcion no valida, saliendo del juego...")
            return False

    # Metodo principal para ejecutar el juego completo
    def jugar(self):
        time.sleep(3)
        salir = True
        while salir:
            if self.personajeJugador.getVida() > 0 or self.personajeCPU.getVida() > 0:
                print("Personaje: " + str(self.personajeJugador) + "\nVida: " + str(self.personajeJugador.getVida())
                      + "\nEscudo: " + str(self.personajeJugador.getEscudo()) + "\n***VS*** " + "\nPersonaje: " + str(
                    self.personajeCPU) + "\nVida: " + str(self.personajeCPU.getVida()) + "\nEscudo: " + str(
                    self.personajeCPU.getEscudo()))
                if self.turno == 1:
                    self.turnoJugador()
                else:
                    self.turnoCPU()
                if self.personajeJugador.getVida() <= 0:
                    print("Has perdido la partida, el personaje " + str(self.personajeCPU.getNom()) + " te ha ganado.")
                    punto = 0
                    salir = False
                elif self.personajeCPU.getVida() <= 0:
                    print("Eres un maquina, tu personaje " + str(self.personajeJugador.getNom()) + " ha ganado con "
                          + str(self.personajeJugador.getVida()) + " de vida.")
                    punto = 1
                    salir = False

        self.setContadorVictoria(punto)