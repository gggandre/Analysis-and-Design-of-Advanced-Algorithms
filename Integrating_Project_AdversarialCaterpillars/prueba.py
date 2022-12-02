from dagor import JuegoOrugas, JugadorOrugasAleatorio
from equipo11 import JugadorOrugasEquipo11


jugador1 = JugadorOrugasAleatorio('Liga MX')
jugador2 = JugadorOrugasEquipo11('Los Pumas')
juego = JuegoOrugas(jugador1, jugador2, 8, 9)
juego.inicia(veces=100, delta_max=2)
