# ----------------------------------------------------------
# Lab #5: Graph Cycle Detection
#
# Date: 07-Oct-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------

# Importing the Enum class from the enum module and the Optional class from
# the typing module.
from enum import Enum
from typing import Optional

# A type hint that tells us that the variable graph is a dictionary that has
# strings as keys and lists
# of strings as values.
Graph = dict[str, list[str]]


def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    """
    It returns a list of nodes that form a cycle if there is one, otherwise it
    returns None
    :param initial: str: The initial node to start the search from
    :type initial: str
    :param graph: Graph = {
    :type graph: Graph
    :return: A list of nodes that form a cycle.
    """
    # All the nodes have the unvisited status
    node_status: dict[str, ConditionNode] = {key: ConditionNode.not_go
                                             for key in graph.keys()}

    node_parents: dict[str, str] = dict()
    return depth_first_search(graph, node_status, node_parents, initial)


def path_cycle(actual: str,
               root: str,
               parents: dict[str, str]) -> list[str]:
    """
    It takes a starting node, a root node, and a dictionary of parents, and
    returns a list of nodes that
    form a cycle
    :param actual: the current node
    :type actual: str
    :param root: The root node of the graph
    :type root: str
    :param parents: dict[str, str]
    :type parents: dict[str, str]
    :return: A list of strings.
    """
    path: list[str] = list()
    path.append(root)
    while actual != root:
        path.append(actual)
        actual = parents[actual]
    path.append(actual)
    path.reverse()
    return path


# The class ConditionNode is an enumeration of the values not_go, Alive, and go
class ConditionNode(Enum):
    not_go = 1
    Alive = 2
    go = 3


def depth_first_search(adj_list: Graph,
                       condition: dict[str, ConditionNode],
                       parent: dict[str, str],
                       actual: str) -> Optional[list[str]]:
    """
    It takes a graph, a dictionary of conditions, a dictionary of parents, and
    a node, and returns a
    cycle if there is one, or None if there isn't

    :param adj_list: Graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'],
    'D': ['C'], 'E': ['F'], 'F':
    ['C']}
    :type adj_list: Graph
    :param condition: dict[str, ConditionNode]
    :type condition: dict[str, ConditionNode]
    :param parent: dict[str, str]
    :type parent: dict[str, str]
    :param actual: str - the current node
    :type actual: str
    :return: A list of nodes that form a cycle.
    """
    cycle: Optional[list[str]] = None
    condition[actual] = ConditionNode.Alive
    for neighbro in adj_list[actual]:
        if (actual in parent
           and neighbro == parent[actual]):
            continue
        if condition[neighbro] == ConditionNode.Alive:
            return path_cycle(actual, neighbro, parent)
        elif condition[neighbro] == ConditionNode.not_go:
            parent[neighbro] = actual
            cycle = depth_first_search(adj_list, condition, parent, neighbro)
            if cycle is not None:
                return cycle
    condition[actual] = ConditionNode.go
    return None


# A conditional statement that checks if the file is being run as a script or
# imported as a module.
if __name__ == '__main__':
    print(has_cycle('A', {'A': ['B'],
                    'B': ['A', 'D'],
                    'C': ['D', 'E'],
                    'D': ['C', 'E'],
                    'E': ['C', 'D']}))
