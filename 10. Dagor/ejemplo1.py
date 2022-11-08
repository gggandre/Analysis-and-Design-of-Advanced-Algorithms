from dagor import JuegoD10, JugadorD10Interactivo, JugadorD10Estrategico 

jugador1 = JugadorD10Interactivo('Profe') 
jugador2 = JugadorD10Interactivo('Máquina') 
juego = JuegoD10(jugador1, jugador2) 
juego.inicia()
