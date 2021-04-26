from Personaje import Personaje
from Tecnica import Tecnica
import random
import time


class Juego:
    def __init__(self):
        self.personajes = []
        self.personajeJugador = Personaje
        self.personajeCPU = Personaje
        self.turno = 1

    def CreacionPersonajes(self):
        t1_p1 = Tecnica("Hulk Aplasta", 150, 30)
        t2_p1 = Tecnica("Hulk Furioso", 180, 1)
        t3_p1 = Tecnica("Añadir Escudo", 0, 30)
        t1_p2 = Tecnica("Pegar", 130, 30)
        t2_p2 = Tecnica("Ataque Crítico", 150, 3)
        t3_p2 = Tecnica("Añadir Escudo", 0, 30)
        t1_p3 = Tecnica("Estabilizadores de Vuelo", 150, 30)
        t2_p3 = Tecnica("Concentración Láser", 180, 3)
        t3_p3 = Tecnica("Añadir Escudo", 0, 30)
        t1_p4 = Tecnica("Iron Man Aplasta", 80, 30)
        t2_p4 = Tecnica("Veronica", 120, 3)
        t3_p4 = Tecnica("Añadir Escudo", 0, 30)
        t1_p5 = Tecnica("Lanzatelarañas", 120, 30)
        t2_p5 = Tecnica("El cosquilleo de Peter", 150, 3)
        t3_p5 = Tecnica("Añadir Escudo", 0, 30)
        t1_p6 = Tecnica("Lanzatelarañas", 150, 30)
        t2_p6 = Tecnica("Matanza Instantánea", 190, 3)
        t3_p6 = Tecnica("Añadir Escudo", 0, 30)
        t1_p7 = Tecnica("Lanzamiento del Escudo", 150, 30)
        t2_p7 = Tecnica("Aguantaría todo el dia", 190, 3)
        t3_p7 = Tecnica("Añadir Escudo", 0, 30)
        t1_p8 = Tecnica("Golpe con brazo metálico", 150, 30)
        t2_p8 = Tecnica("Ataque Hydra", 190, 3)
        t3_p8 = Tecnica("Añadir Escudo", 0, 30)
        t1_p9 = Tecnica("Ataque Básico", 180, 30)
        t2_p9 = Tecnica("Gemas del Infinito", 220, 3)
        t3_p9 = Tecnica("Añadir Escudo", 0, 30)
        t1_p10 = Tecnica("Llave de combate", 150, 30)
        t2_p10 = Tecnica("Entrenamiento Natasha", 180, 3)
        t3_p10 = Tecnica("Añadir Escudo", 0, 30)
        t1_p11 = Tecnica("Disparar Flecha", 150, 30)
        t2_p11 = Tecnica("Te he hecho mirar", 180, 3)
        t3_p11 = Tecnica("Añadir Escudo", 0, 30)
        t1_p12 = Tecnica("Ala Roja", 150, 30)
        t2_p12 = Tecnica("Por la Izquierda", 180, 3)
        t3_p12 = Tecnica("Añadir Escudo", 0, 30)
        t1_p13 = Tecnica("Estabilizadores de Vuelo", 150, 30)
        t2_p13 = Tecnica("Concentración Láser", 180, 3)
        t3_p13 = Tecnica("Añadir Escudo", 0, 30)

        personaje1 = Personaje("Hulk", "Tanque", 150, 900, 0, t1_p1, t2_p1, t3_p1)
        personaje2 = Personaje("Profesor Hulk", "Tanque", 130, 900, 0, t1_p2, t2_p2, t3_p2)
        personaje3 = Personaje("Iron Man Mark 50", "Versátil", 150, 600, 0, t1_p3, t2_p3, t3_p3)
        personaje4 = Personaje("Iron Man HulkBuster", "Tanque", 80, 1000, 0, t1_p4, t2_p4, t3_p4)
        personaje5 = Personaje("Spider-Man", "Versátil", 120, 600, 0, t1_p5, t2_p5, t3_p5)
        personaje6 = Personaje("Spider-Man Iron Spider", "Versátil", 150, 600, 0, t1_p6, t2_p6, t3_p6)
        personaje7 = Personaje("Capitan America", "Versátil", 150, 600, 0, t1_p7, t2_p7, t3_p7)
        personaje8 = Personaje("Lobo Blanco", "Versátil", 150, 600, 0, t1_p8, t2_p8, t3_p8)
        personaje9 = Personaje("Thanos", "Titán", 180, 900, 0, t1_p9, t2_p9, t3_p9)
        personaje10 = Personaje("Viuda Negra", "Espia", 120, 450, 0, t1_p10, t2_p10, t3_p10)
        personaje11 = Personaje("Hawkeye", "Espia", 120, 450, 0, t1_p11, t2_p11, t3_p11)
        personaje12 = Personaje("Falcon", "Aéreo", 120, 450, 0, t1_p12, t2_p12, t3_p12)
        personaje13 = Personaje("Maquina de Guerra", "Versátil", 150, 600, 0, t1_p13, t2_p13, t3_p13)

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

    def listarPersonajes(self):
        print("**Personajes Disponibles**")
        for x in range(0, len(self.personajes)):
            print(self.personajes[x])

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

    def elegirPersonajeCPU(self):
        personajeAleatorio = random.choice(self.personajes)
        self.personajeCPU = personajeAleatorio
        self.personajes.remove(personajeAleatorio)
        print("Jugador elegido por la CPU: " + str(self.personajeCPU))

    def bajarVidaCPU(self, tecnica):
        if self.personajeCPU.getEscudo() == 0:
            self.personajeCPU.setVida(self.personajeCPU.getVida() - tecnica.getDano())
        else:
            self.personajeCPU.setEscudo(self.personajeCPU.getEscudo() - tecnica.getDano())
            if self.personajeCPU.getEscudo() < 0:
                self.personajeCPU.setVida(self.personajeCPU.getVida() - abs(self.personajeCPU.getEscudo()))
                self.personajeCPU.setEscudo(0)

    def bajarVidaJugador(self, tecnica):
        if self.personajeJugador.getEscudo() == 0:
            self.personajeJugador.setVida(self.personajeJugador.getVida() - tecnica.getDano())
        else:
            self.personajeJugador.setEscudo(self.personajeJugador.getEscudo() - tecnica.getDano())
            if self.personajeJugador.getEscudo() < 0:
                self.personajeJugador.setVida(self.personajeJugador.getVida() - abs(self.personajeJugador.getEscudo()))
                self.personajeJugador.setEscudo(0)

    def getTecnicaContador(self, tecnica):
        return tecnica.getContador()

    def setTecnicaContador(self, tecnica, num):
        tecnica.setContador(num)

    def turnoJugador(self):
        self.turno = 2
        print("Comienza el turno del Usuario...")
        time.sleep(3)
        print("Tecnicas del Personaje: " + "\n1.- " + str(self.personajeJugador.getTecnica(1)) + "\n2.- "
              + str(self.personajeJugador.getTecnica(2)) + "\n3.- " + str(self.personajeJugador.getTecnica(3)))
        tecnicaEscogida = int(input("¿Qué tecnica querrías usar? "))
        numRandomEsquivar = random.choice(range(1, 100))
        time.sleep(4)
        if numRandomEsquivar < 90:
            if self.personajeJugador.getTecnica(tecnicaEscogida).getContador() > 0:
                self.bajarVidaCPU(self.personajeJugador.getTecnica(tecnicaEscogida))
                if tecnicaEscogida == 3:
                    self.personajeJugador.setEscudo(150)
            else:
                print("Ya no se puede usar mas")
        else:
            print("El personaje " + str(self.personajeCPU.getNom()) + " ha esquivado el ataque")

    def turnoCPU(self):
        self.turno = 1
        print("Comienza el turno de la CPU...")
        time.sleep(3)
        print("Tecnicas del Personaje: " + "\n1.- " + str(self.personajeCPU.getTecnica(1)) + "\n2.- "
              + str(self.personajeCPU.getTecnica(2)) + "\n3.- " + str(self.personajeCPU.getTecnica(3)))
        print("Eligiendo con sabiduria :) ...")
        time.sleep(3)
        numRandom = random.choice(range(1, 4))
        numRandomEsquivar = random.choice(range(1, 100))
        time.sleep(4)
        if numRandomEsquivar < 90:
            if self.personajeCPU.getTecnica(numRandom).getContador() > 0:
                self.bajarVidaJugador(self.personajeCPU.getTecnica(numRandom))
                if numRandom == 3:
                    self.personajeCPU.setEscudo(150)
            else:
                print("Ya no se puede usar mas")
        else:
            print("El personaje " + str(self.personajeJugador.getNom()) + " ha esquivado el ataque")

    def volverJugar(self):
        volverJuego = input("¿Deseas volver a jugar? [s/n]")
        if volverJuego == "s":
            return True
        elif volverJuego == "n":
            return False
        else:
            print("Opcion no valida, saliendo del juego...")
            return False

    def jugar(self):
        time.sleep(2)
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
                    print("Has perdido la partida, el personaje " + str(self.personajeCPU.getNom())+" te ha ganado.")
                    salir = False
                elif self.personajeCPU.getVida() <= 0:
                    print("Eres un maquina, tu personaje " + str(self.personajeJugador.getNom()) + " ha ganado con "
                          + str(self.personajeJugador.getVida()) + " de vida.")
                    salir = False

