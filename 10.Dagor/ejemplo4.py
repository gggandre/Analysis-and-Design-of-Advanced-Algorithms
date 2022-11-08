from dagor import JuegoOrugas, JugadorOrugasInteractivo
from dagor import JugadorOrugasAleatorio

jugador1 = JugadorOrugasAleatorio('Cosa 1')
jugador2 = JugadorOrugasAleatorio('Machine')
juego = JuegoOrugas(jugador1, jugador2, 10, 10)
juego.inicia(veces=100)
