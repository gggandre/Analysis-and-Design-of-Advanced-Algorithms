# code made in class with teacher ariel
# A01753176 Gilberto André García Gaytán
def powers_of_two(n: int) -> list[int]:
    return [2 ** x for x in range(n)]


if __name__ == '__main__':
    print(powers_of_two(10))