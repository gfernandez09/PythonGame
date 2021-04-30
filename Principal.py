from Juego import Juego

jugar = True
contador = 0
while jugar:
    juego = Juego()
    juego.setContadorVictoria(contador)
    juego.CreacionPersonajes()
    juego.listarPersonajes()
    juego.elegirPersonajeJugador()
    juego.elegirPersonajeCPU()
    juego.jugar()
    jugar = juego.volverJugar()
    ganado = juego.getContadorVictoria()
    contador += ganado
