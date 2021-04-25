from Personaje import Personaje
from Tecnica import Tecnica
import random
import time


class Juego:
    def __init__(self):
        self.personajes = []
        self.personajeJugador = Personaje
        self.personajeCPU = Personaje

    def CreacionPersonajes(self):
        t1_p1 = Tecnica("Hulk Aplasta", 150, 5)
        t2_p1 = Tecnica("Hulk Furioso", 180, 3)
        t3_p1 = Tecnica("Añadir Escudo", 0, 5)
        t1_p2 = Tecnica("Pegar", 130, 5)
        t2_p2 = Tecnica("Ataque Crítico", 150, 3)
        t3_p2 = Tecnica("Añadir Escudo", 0, 5)
        t1_p3 = Tecnica("Estabilizadores de Vuelo", 150, 5)
        t2_p3 = Tecnica("Concentración Láser", 180, 3)
        t3_p3 = Tecnica("Añadir Escudo", 0, 5)
        t1_p4 = Tecnica("Iron Man Aplasta", 80, 5)
        t2_p4 = Tecnica("Veronica", 120, 3)
        t3_p4 = Tecnica("Añadir Escudo", 0, 5)
        t1_p5 = Tecnica("Lanzatelarañas", 120, 5)
        t2_p5 = Tecnica("El cosquilleo de Peter", 150, 3)
        t3_p5 = Tecnica("Añadir Escudo", 0, 5)
        t1_p6 = Tecnica("Lanzatelarañas", 150, 5)
        t2_p6 = Tecnica("Matanza Instantánea", 190, 3)
        t3_p6 = Tecnica("Añadir Escudo", 0, 5)
        t1_p7 = Tecnica("Lanzamiento del Escudo", 150, 5)
        t2_p7 = Tecnica("Aguantaría todo el dia", 190, 3)
        t3_p7 = Tecnica("Añadir Escudo", 0, 5)
        t1_p8 = Tecnica("Golpe con brazo metálico", 150, 5)
        t2_p8 = Tecnica("Ataque Hydra", 190, 3)
        t3_p8 = Tecnica("Añadir Escudo", 0, 5)
        t1_p9 = Tecnica("Ataque Básico", 180, 5)
        t2_p9 = Tecnica("Gemas del Infinito", 220, 3)
        t3_p9 = Tecnica("Añadir Escudo", 0, 5)
        t1_p10 = Tecnica("Llave de combate", 120, 5)
        t2_p10 = Tecnica("Entrenamiento Natasha", 150, 3)
        t3_p10 = Tecnica("Añadir Escudo", 0, 5)
        t1_p11 = Tecnica("Disparar Flecha", 120, 5)
        t2_p11 = Tecnica("Te he hecho mirar", 150, 3)
        t3_p11 = Tecnica("Añadir Escudo", 0, 5)
        t1_p12 = Tecnica("Ala Roja", 120, 5)
        t2_p12 = Tecnica("Por la Izquierda", 150, 3)
        t3_p12 = Tecnica("Añadir Escudo", 0, 5)
        t1_p13 = Tecnica("Estabilizadores de Vuelo", 150, 5)
        t2_p13 = Tecnica("Concentración Láser", 150, 3)
        t3_p13 = Tecnica("Añadir Escudo", 0, 5)

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

    def bajarVidaJugador(self, tecnica):
        if self.personajeJugador.getEscudo() == 0:
            self.personajeJugador.setVida(self.personajeJugador.getVida() - tecnica.getDano())
        else:
            self.personajeJugador.setEscudo(self.personajeJugador.getEscudo() - tecnica.getDano())

    def turnoJugador(self):
        print("Comienza el turno del Usuario...")
        time.sleep(3)
        print("Tecnicas del Personaje: " + "\n" + self.personajeJugador.getTecnica(1) + "\n"
              + self.personajeJugador.getTecnica(2) + "\n" + self.personajeJugador.getTecnica(3))
        tecnicaEscogida = int(input("¿Qué tecnica querrías usar? "))
        self.bajarVidaCPU(self.personajeJugador.getTecnica(tecnicaEscogida))

    def jugar(self):
        # while self.personajeJugador.getVida() > 0 or self.personajeCPU.getVida() > 0:
        print(str(self.personajeJugador) + " " + str(self.personajeJugador.getVida()) + " ***VS*** " + str(
            self.personajeCPU) + " " + str(self.personajeCPU.getVida()))
