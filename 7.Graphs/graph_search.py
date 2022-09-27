from inspect import stack
from typing import Generator
from collections import deque


Graph = dict[str, list[str]]

g: Graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'D'],
    'C': ['A', 'E', 'F'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['A', 'C', 'E', 'G'],
    'G': ['F']
}


def breadth_first_search(
        start: str,
        graph: Graph) -> Generator[str, None, None]:
    queue: deque[str] = deque()
    visited: set[str] = set()
    queue.append(start)
    while queue:
        current: str = queue.popleft()
        if current not in visited:
            yield current
            queue.extend(graph[current])
            visited.add(current)


def depth_first_search(
        start: str,
        graph: Graph) -> Generator[str, None, None]:
    stack: deque[str] = deque()
    visited: set[str] = set()
    stack.append(start)
    while stack:
        current: str = stack.pop()
        if current not in visited:
            yield current
            stack.extend(graph[current][::-1])  # reverse your collection
            visited.add(current)


# def pow2(n: int) -> Generator[int, None, None]:
#   for i in range(n):
#        yield 2 ** 1


if __name__ == '__main__':
    # generator = pow2(10)
    # print(next(generator))
    # print(next(generator))
    # print(next(generator))
    # print(next(generator))
    # for n in generator:
    #    print(n)
    # print(tuple(generator))
    print(list(depth_first_search('A', g)))
    print(list(breadth_first_search('A', g)))

    x = 'C'
    for i, y in enumerate(depth_first_search('A', g)):
        if y == x:
            print(i)
            break
    else:
        print('Not found')
