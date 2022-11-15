# ----------------------------------------------------------
# Lab #7: Tries & String Prefixes
#
# Date: 04-Nov-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------

# Importing the annotations from the future, the Iterator from the
# collections.abc, and the Generic,
# Optional, and TypeVar from the typing.
from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, Optional, TypeVar

# Getting the number of letters in the alphabet.
NUM_LETTERS = ord('z') - ord('a') + 1

T = TypeVar('T')  # Generic type for the Tier class
N = TypeVar('N')  # Generic type for the nested Node class


class Trie(Generic[T]):

    __keys: int

    # It's a node in a trie
    class Node(Generic[N]):

        __children: list[Optional[Trie.Node[N]]]
        __num_children: int
        value: Optional[N]

        def __init__(self) -> None:
            """
            The function initializes the children of the node to be an array
            of size 26, and sets the
            number of children to 0
            """
            self.__children = ([None] * NUM_LETTERS)
            self.__num_children = 0
            self.value = None

        def __len__(self) -> int:
            """
            This function returns the number of children in the tree
            :return: The number of children in the family.
            """
            return self.__num_children

        def __bool__(self) -> bool:
            """
            This function returns True if the object is considered true, and
            False if it is considered false
            :return: True
            """
            return True

        def __getitem__(self, index: int) -> Optional[Trie.Node[N]]:
            """
            This function returns the child node at the given index
            :param index: The index of the child node to get
            :type index: int
            :return: The node at the given index.
            """
            return self.__children[index]

        def __setitem__(
                self,
                index: int,
                value: Optional[Trie.Node[N]]) -> None:
            self.__children[index] = value
            self.__num_children += 1

        def __iter__(self) -> Iterator:
            return iter(self.__children)

    __root: Trie.Node[T]

    def __init__(self) -> None:
        self.__root = Trie.Node()
        self.__keys = 0

    def insert(self, key: str, value: T) -> None:
        """
        If the current node is a node, and the current node's value is None,
        then increment the number of keys by 1

        :param key: str
        :type key: str
        :param value: T
        :type value: T
        """
        current: Optional[Trie.Node[T]] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if isinstance(current, Trie.Node):
                if not current[i]:
                    current[i] = Trie.Node()
                current = current[i]
        if isinstance(current, Trie.Node):
            if current.value is None:
                self.__keys += 1
            current.value = value

    def search(self, key: str) -> Optional[T]:
        """
        If the current node is a node, and the current node's child at index i
        is not None,then set the current node to the current node's child at
        index i

        :param key: str
        :type key: str
        :return: The value of the key.
        """
        current: Optional[Trie.Node[T]] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if isinstance(current, Trie.Node):
                if not current[i]:
                    return None
                current = current[i]
        if isinstance(current, Trie.Node):
            return current.value
        return None

    def remove(self, key: str) -> bool:
        """
        If the key is in the trie, remove it and return True, otherwise return
        False

        :param key: str
        :type key: str
        :return: The value associated with the key.
        """
        current: Optional[Trie.Node[T]] = self.__root
        for c in key:
            i: int = Trie.__c2i(c)
            if isinstance(current, Trie.Node):
                if not current[i]:
                    return False
                current = current[i]
        if isinstance(current, Trie.Node):
            if current.value is not None:
                current.value = None
                self.__keys -= 1
                return True
        return False

    def __len__(self) -> int:
        """
        This function returns the number of keys in the dictionary
        :return: The number of keys in the dictionary.
        """
        return self.__keys

    def items(self) -> list[tuple[str, T]]:
        """
        It returns a list of tuples of strings and T.
        :return: A list of tuples.
        """
        items: list[tuple[str, T]] = []
        current: Optional[Trie.Node[T]] = self.__root
        if isinstance(current, Trie.Node):
            self.__itemsR__(current, '', items)
            return items
        return []

    def prefixes(self) -> dict[str, set[str]]:
        """
        The function takes a trie and returns a dictionary of all the
        prefixes in the trie and the words that have that prefix
        :return: A dictionary of prefixes and the words that have that prefix.
        """
        prefixes: dict[str, set[str]] = dict()
        activeP: list[str] = []
        current: Optional[Trie.Node[T]] = self.__root
        if isinstance(current, Trie.Node):
            self.__prefixesR__(current, '',
                               activeP,
                               prefixes)
        return prefixes

    def __itemsR__(self, current_node: Trie.Node[T],
                   current_key: str,
                   items: list[tuple[str, T]]) -> None:
        """
        If the current node has a value, add the current key and the value to
        the list of items. Then, for each child of the current node, if the
        child is a node, recursively call the function with the child as the
        current node, the current key plus the child's letter as the current
        key, and the list of items

        :param current_node: Trie.Node[T]
        :type current_node: Trie.Node[T]
        :param current_key: str
        :type current_key: str
        :param items: list[tuple[str, T]]
        :type items: list[tuple[str, T]]
        """
        if current_node.value is not None:
            items.append((current_key, current_node.value))
        for i in range(NUM_LETTERS):
            child: Optional[Trie.Node[T]] = current_node[i]
            if isinstance(child, Trie.Node):
                self.__itemsR__(child,
                                current_key + self.__i2c(i),
                                items)

    def __prefixesR__(self, current_node: Trie.Node[T],
                      current_key: str,
                      active_prefixes: list[str],
                      prefixes: dict[str, set[str]]):
        """
        It recursively traverses the trie, adding the current key to the active
        prefixes list if the current node is a leaf, and then recursively
        traversing the children of the current node

        :param current_node: Trie.Node[T]
        :type current_node: Trie.Node[T]
        :param current_key: str
        :type current_key: str
        :param active_prefixes: list[str]
        :type active_prefixes: list[str]
        :param prefixes: dict[str, set[str]]
        :type prefixes: dict[str, set[str]]
        """
        prefix_added: bool = False
        if current_node.value is not None:
            for prefix in active_prefixes:
                if prefix not in prefixes:
                    prefixes[prefix] = set()
                prefixes[prefix].add(current_key)
            active_prefixes.append(current_key)
            prefix_added = True

        for i in range(NUM_LETTERS):
            child: Optional[Trie.Node[T]] = current_node[i]
            if isinstance(child, Trie.Node):
                self.__prefixesR__(child,
                                   current_key + self.__i2c(i),
                                   active_prefixes,
                                   prefixes)

        if prefix_added:
            active_prefixes.pop()

    @staticmethod
    def __c2i(c: str) -> int:
        return ord(c.lower()) - ord('a')

    @staticmethod
    def __i2c(i: int) -> str:
        return chr(i + ord('a'))


if __name__ == '__main__':
    t: Trie[int] = Trie()
    t.insert("america", 1)
    t.insert("insert", 2)
    t.insert("prueba", 5)
    t.insert("pr", 2)
    t.insert("ame", 4)
    print(len(t))
    print(t.items())
    print(t.prefixes())
