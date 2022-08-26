# code made in class with teacher ariel
# A01753176 Gilberto André García Gaytán
def sevens(n: int) -> list:
    return [x for x in range(n + 1)
            if x % 7 == 0 or x % 10 == 7]


if __name__ == '__main__':
    from pprint import pprint

    pprint(sevens(100))
