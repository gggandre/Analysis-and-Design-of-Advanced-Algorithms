while len(queue)>0:
            (r, c, distancia)=queue.popleft()

            # Checar arriba
            if r > 0:
                i = r - 1
            else:
                i = self.juego.renglones - 1
            j = c

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1

            # Checar derecha
            if c < (self.juego.columnas - 1):
                j = c + 1
            else:
                j = 0
            i = r

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1

            # Checar abajo
            if r < (self.juego.renglones - 1):
                i = r + 1
            else:
                i = 0
            j = c

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1

            # Checar izquierda
            if c > 0:
                j = c - 1
            else:
                j = self.juego.columnas - 1
            i = r

            if self.distancias[jugador][i][j] == '*' and tablero[i][j] == ' ':
                queue.append((i, j, distancia + 1))
                self.distancias[jugador][i][j] = distancia + 1