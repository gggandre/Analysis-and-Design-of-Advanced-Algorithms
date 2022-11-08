from dagor import JuegoSuperGato, JugadorSuperGatoInteractivo, JuegoD10
from dagor import JugadorSuperGatoEstrategico

jugador1 = JugadorSuperGatoInteractivo('Cosa 1')
jugador2 = JugadorSuperGatoEstrategico('Cosa 2')
juego = JuegoSuperGato(jugador1, jugador2, 3, 4)
juego.inicia()
