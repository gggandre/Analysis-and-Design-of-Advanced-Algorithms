from dagor import JuegoOrugas, JugadorOrugasInteractivo
from dagor import JugadorOrugasAleatorio

jugador1 = JugadorOrugasInteractivo('Cosa 1')
jugador2 = JugadorOrugasAleatorio('Machine')
juego = JuegoOrugas(jugador1, jugador2, 4, 4)
juego.inicia()
