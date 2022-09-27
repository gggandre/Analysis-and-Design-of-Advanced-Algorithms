# ----------------------------------------------------------
# Lab #4: Cryptarithmetic with CSP
# General cryptarithmetic puzzle solver.
#
# Date: 27-Sep-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------
from csp import Constraint, CSP
from typing import Optional



if __name__ == '__main__':
    print(solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes'))
