from Juego import Juego

jugar = True
while jugar:
    juego = Juego()
    juego.CreacionPersonajes()
    juego.listarPersonajes()
    juego.elegirPersonajeJugador()
    juego.elegirPersonajeCPU()
    juego.jugar()
    jugar = juego.volverJugar()
