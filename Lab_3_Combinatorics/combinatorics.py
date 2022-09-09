# ----------------------------------------------------------
# Lab #3: Combinatorics
# Permutations and combinations with repetition.
#
# Date: 09-Sep-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------
from comparable import C
from pprint import pprint


def power_set(s: list[C]) -> list[list[C]]:
    if s:
        r = power_set(s[:-1])
        return r + [t + [s[-1]] for t in r]
    else:
        return [[]]


def sorted_nicely(s: list[list[C]]) -> list[list[C]]:

    def compare_by_size_and_content(t: list[C]) -> tuple[int, list[C]]:
        return (len(t), t)

    return sorted(s, key=compare_by_size_and_content)


def combinations(s: list[C], n: int) -> list[list[C]]:
    return [t for t in power_set(s) if len(t) == n]


def insert(x: C, lst: list[C], i: int) -> list[C]:
    return lst[:i] + [x] + lst[i:]


def insert_many(x: C, lst: list[C]) -> list[list[C]]:
    return [insert(x, lst, i) for i in range(len(lst) + 1)]


def permute(s: list[C]) -> list[list[C]]:
    if s:
        r = permute(s[:-1])
        return sum([insert_many(s[-1], t) for t in r], [])
    else:
        return [[]]


def permutations(s: list[C], n: int) -> list[list[C]]:
    return sum([permute(t) for t in combinations(s, n)], [])


def permutations_with_repetition(s: list[C], n: int) -> list[list[C]]:
    if n == 0:
        return []
    else:
        if n - 1 == 0:
            next_permutation: list[list[C]] = [[]]
        else:
            next_permutation = permutations_with_repetition(s, n - 1)
        return [insert(elem, permutation, 0)
                for elem in s
                for permutation in next_permutation]


def combinations_with_repetition(s: list[C], n: int) -> list[list[C]]:

    if n == 0:
        return []
    permutations = permutations_with_repetition(s, n)
    combinations = [sorted(item) for item in permutations]
    return [list(item) for item in set(tuple(row) for row in combinations)]


if __name__ == '__main__':

    pprint(sorted_nicely(power_set([1, 2, 3, 4])))
    print()
    pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 2)))
    print()
    pprint(sorted_nicely(combinations([True, False], 1)))
    print()
    pprint(permutations_with_repetition(['a', 'b', 'c'], 2))
    pprint(combinations_with_repetition(['a', 'b', 'c'], 2))
    pprint(permute([1, 2, 3]))
