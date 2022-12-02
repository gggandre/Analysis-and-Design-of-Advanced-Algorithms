# ----------------------------------------------------------
# Project: Adversarial Caterpillars
#
# Date: 01-Dec-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------

# It imports the deque class from the collections module.
from collections import deque
# It imports the choice function from the random module.
from random import choice
# It imports the class JugadorOrugas from the file dagor.py
from dagor import JugadorOrugas


# It uses a heuristic function to determine the best possible move for the
# computer
class JugadorOrugasEquipo11(JugadorOrugas):
    # A list of lists of lists, which is used to store the distance from the
    # head of each snake to
    # every other point on the grid.
    distance: list[list[list]]

    def check(self, position):
        """
        It checks the distance between the two caterpillars'
        heads and the rest of the board
        :param position: The current game state
        :return: The difference between the number of good and bad positions.
        """
        grid = position[1]
        self.distance = [[[10 for c in range(self.juego.columnas)]
                          for r in range(self.juego.renglones)]
                         for k in range(2)]
        for r in range(self.juego.renglones):
            for c in range(self.juego.columnas):
                if grid[r][c] == self.simbolo:
                    rOur_head = r
                    cOurHead = c
                elif grid[r][c] == self.contrario.simbolo:
                    rYourHead = r
                    cYourhead = c
        self.searchEnemy(rOur_head, cOurHead, 0, grid)
        self.searchEnemy(rYourHead, cYourhead, 1, grid)
        bad = 0
        good = 0
        for r in range(self.juego.renglones):
            for c in range(self.juego.columnas):
                if self.distance[0][r][c] > self.distance[1][r][c]:
                    bad += 1
                elif self.distance[0][r][c] < self.distance[1][r][c]:
                    good += 1
        return good-bad

    def searchEnemy(self, rHead, cHead, player, grid):
        """
        It takes the head of the snake, the player number, and the grid,
        and it fills the distance array with the distance from the head
        to every other point on the grid
        :param rHead: row of the head of the snake
        :param cHead: column of the head of the snake
        :param player: The player number
        :param grid: The grid of the game
        """
        queue = deque()
        queue.append((rHead, cHead, 0))
        while len(queue) > 0:
            (r, c, distance) = queue.popleft()
            if r > 0:
                i = r - 1
            else:
                i = self.juego.renglones - 1
            j = c
            if self.distance[player][i][j] == 10 and grid[i][j] == ' ':
                queue.append((i, j, distance + 1))
                self.distance[player][i][j] = distance + 1
            if c < (self.juego.columnas - 1):
                j = c + 1
            else:
                j = 0
            i = r
            if self.distance[player][i][j] == 10 and grid[i][j] == ' ':
                queue.append((i, j, distance + 1))
                self.distance[player][i][j] = distance + 1
            if r < (self.juego.renglones - 1):
                i = r + 1
            else:
                i = 0
            j = c
            if self.distance[player][i][j] == 10 and grid[i][j] == ' ':
                queue.append((i, j, distance + 1))
                self.distance[player][i][j] = distance + 1
            if c > 0:
                j = c - 1
            else:
                j = self.juego.columnas - 1
            i = r
            if self.distance[player][i][j] == 10 and grid[i][j] == ' ':
                queue.append((i, j, distance + 1))
                self.distance[player][i][j] = distance + 1

    def heuristica(self, position, depth, alpha, beta):
        """
        It's a recursive function that returns the maximum value of the
        heuristic function for a given position
        :param position: the current board state
        :param depth: the depth of the search tree
        :param alpha: the best score that the maximizing player can guarantee
        given the current state of the game :param beta: the best value that
        the maximizing player can guarantee given the current information
        :return: The maximum value of the heuristic function.
        """
        Alpha = alpha
        if self.triunfo(position) is not None:
            return -1E999
        if depth == 0:
            return self.check(position)
        possibility = self.posiciones_siguientes(position)
        maximum = -1E9999

        for p in possibility:
            d = -self.heuristica(position, depth - 1, -beta, -Alpha)
            if d > maximum:
                maximum = d
            if maximum >= beta:
                break
            if maximum > Alpha:
                Alpha = maximum
        return maximum

    def tira(self, posicion):
        """
        It returns the best possible move for the computer,
        based on the current state of the board.
        :param posicion: the current board state
        :return: The best option
        """
        possibles = self.posiciones_siguientes(posicion)
        best_score = -1E999
        best_option = choice(possibles)
        for p in possibles:
            puntaje = self.heuristica(p, 6, -1E999, 1E999)
            if puntaje > best_score:
                best_score = puntaje
                best_option = p
        return best_option
