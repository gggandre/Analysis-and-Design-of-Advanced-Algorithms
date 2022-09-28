# ----------------------------------------------------------
# Lab #4: Cryptarithmetic with CSP
# General cryptarithmetic puzzle solver.
#
# Date: 27-Sep-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------
from typing import Optional
from csp import Constraint, CSP


# `CSPConstraint` is a subclass of `Constraint` that takes a list of letters,
# a list of additions, and
# a result
class CSPConstraint(Constraint[str, int]):
    def __init__(self,
                 letters: list[str],
                 additions: list[str],
                 result: str) -> None:
        super().__init__(letters)
        self.variables: list[str] = letters
        self.additions = additions
        self.expected_result: str = result

    def num(self, word: str, values: dict[str, int]):
        """
        It takes a word and a dictionary of letters and their values, and
        returns the sum of the values
        of the letters in the word
        :param word: str = The word to be converted to a number
        :type word: str
        :param values: dict[str, int]
        :type values: dict
                    [str, int]
        :return: the addition of the values of the letters in the word.
        """
        addition: int = 0
        base: int = 1
        for letter in reversed(word):
            addition += values[letter] * base
            base *= 10
        return addition

    def satisfy(self, assignment: dict[str, int]):
        """
        If the number of unique values in the assignment is less than the
        number of variables, then the assignment is not complete, so return
        True. Otherwise, if the number of variables in the
        assignment is less than the number of variables in the problem, then
        the assignment is not complete, so return True. Otherwise, if the sum
        of the numbers represented by the words in the additions list is equal
        to the number represented by the expected result, then the assignment
        is complete and correct, so return True. Otherwise, the assignment is
        complete and incorrect, so return False
        :param assignment: dict[str, int]
        :type assignment: dict[str, int]
        :return: a boolean value.
        """
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) < len(self.variables):
            return True

        addition: int = 0
        for word in self.additions:
            number: int = self.num(word,
                                   assignment)
            addition += number

        return addition == self.num(self.expected_result,
                                    assignment)


def solve_cryptarithmetic_puzzle(
        additions: list[str],
        result: str) -> Optional[dict[str, int]]:

    """
        It takes a list of addition problems and a result, and returns a
        dictionary mapping letters to
        digits if there is a solution, or None if there is no solution
        :param additions: list[str]
        :type additions: list[str]
        :param result: The result of the addition
        :type result: str
        :return: A dictionary of the letters and their corresponding values.
        """
    for n in range(len(additions)):
        additions[n] = additions[n].upper()
    result = result.upper()

    var: set[str] = set()
    for word in additions:
        for letter in word:
            var.add(letter)
    for letter in result:
        var.add(letter.upper())
    letters: list[str] = list(var)
    letters.sort()

    domains: dict[str, list[int]] = {var: list(range(10))
                                     for var in letters}

    csp: CSP[str, int] = CSP(letters, domains)
    csp.add_constraint(CSPConstraint(letters, additions, result))
    solver: Optional[dict[str, int]] = csp.backtracking_search()
    return solver


# A conditional statement that checks if the file is being run as a script or
# imported as a module.
if __name__ == '__main__':
    print(solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes'))
