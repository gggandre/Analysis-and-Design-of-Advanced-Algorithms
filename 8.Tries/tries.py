from __future__ import annotations
from typing import Generic, Optional, TypeVar
from collections.abc import Iterator

NUM_LETTERS = ord('z') - ord('a') + 1

T = TypeVar('T')

class Trie(Generic[T]):

    class Node:

        __children__: list[Optional[Trie.Node]]
        __num_children__: int
        value: Optional[T]

        def __init__(self) -> None:
            self.__children: list[Optional[Trie.Node]] = [None] * NUM_LETTERS
            self.__num_children: int = 0
            self.value: Optional[T] = None

        def __len__(self) -> int:
            return self.__num_children

        def __bool__(self) -> bool:
            return True

        def __getitem__(self, index: int) -> Optional[Trie.Node]:
            return self.__children[index]

        def __setitem__(self, index: int, value: Optional[Trie.Node]) -> None:
            self.__children[index] = value
            self.__num_children += 1

        def __iter__(self) -> Iterator:
            return iter(self.__children)

    def __init__(self) -> None:
        self.__root: Trie.Node = Trie.Node()


    @staticmethod
    def __c2i(c: str) -> int:
        return ord(c.lower()) - ord('a')

    @staticmethod
    def __i2c(i: int) -> str:
        return chr(i + ord('a'))

    def insert(self, key: str, value: T) -> None:
        current: Optional[Trie.Node] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if not current[i]:
                current[i] = Trie.Node()
            current = current[i]
        if isinstance(current, Trie.Node):
            current.value = value

    def search(self, key: str) -> Optional[T]:
        current: Optional[Trie.Node] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if isinstance(current, Trie.Node):
                if not current[i]:
                    return None
                current = current[i]
        if isinstance(current, Trie.Node):
            return current.value
        return None

if __name__ == "__main__":
    t: Trie[int] = Trie()
    t.insert('help', 1)
    t.insert('he', 2)
    t.insert('hello', 3) 
    print(t.search('he'))
    print(t.search('hell'))
    print(t.search('hello'))
    print(t.search('ant'))
