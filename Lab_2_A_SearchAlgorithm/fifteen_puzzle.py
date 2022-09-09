# ---------------------------------------------------------
# Lab #2: A* Search Algorithm
# Solving the 15 puzzle.
#
# Date: 02-Sep-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------
from typing import Optional
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]


def solve_puzzle(frame: Frame) -> None:

    result: Optional[Node[Frame]] = astar(frame, goal_test, successors, heuristic)

    if result is None:
        print('No solution found!')
    else:
        path = node_to_path(result)
        if len(path) - 2 == 0:
            print(f'Solution requires 1 step')
        else:
            print(f'Solution requires {len(path) - 1} steps')

        for i in range(len(path) - 1):
            flat: tuple[int, ...] = tuple(k for tup in path[i] for k in tup)
            flat_next: tuple[int, ...] = \
                tuple(k for tup in path[i + 1] for k in tup)

            columns: int = len(frame[0])
            zero_current: int = flat.index(0)
            zero_next: int = flat_next.index(0)

            direction = ""
            if zero_next == zero_current - columns:
                direction = "down"
            elif zero_next == zero_current + columns:
                direction = "up"
            elif zero_next == zero_current - 1:
                direction = "right"
            elif zero_next == zero_current + 1:
                direction = "left"

            print(f'Step {i + 1}: Move {flat_next[zero_current]} {direction}')


def goal_test(frame: Frame) -> bool:
    if frame == ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0)):
        return True
    else:
        return False


def heuristic(frame: Frame) -> float:
    incorrect_positions = 0.0
    correct_frame = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0))

    for i in range(0, 4):
        for j in range(0, 4):
            if frame[i][j] != correct_frame[i][j]:
                incorrect_positions += 1
    return incorrect_positions


def successors(frame: Frame) -> list[Frame]:
    flat: tuple[int, ...] = tuple(i for tup in frame for i in tup)
    rows: int = len(frame)
    columns: int = len(frame[0])
    zero_index: int = flat.index(0)

    def swap(i1: int, i2: int) -> Frame:
        lst: list[int] = list(flat)
        lst[i1], lst[i2] = lst[i2], lst[i1]
        return tuple(tuple(lst[r * columns:(r + 1) * columns])
                     for r in range(rows))

    # Generate potential successors
    up = swap(zero_index, zero_index - columns) \
        if zero_index >= columns \
        else None
    down = swap(zero_index, zero_index + columns) \
        if zero_index + columns < len(flat) \
        else None
    left = swap(zero_index, zero_index - 1) \
        if zero_index % columns != 0 \
        else None
    right = swap(zero_index, zero_index + 1) \
        if (zero_index + 1) % columns != 0 \
        else None

    return [s for s in (up, down, left, right) if s is not None]


if __name__ == '__main__':
    solve_puzzle(((2, 3, 4, 8),
                  (1, 5, 7, 11),
                  (9, 6, 12, 15),
                  (13, 14, 10, 0)))
