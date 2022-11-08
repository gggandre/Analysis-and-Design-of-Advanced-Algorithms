# ----------------------------------------------------------
# Lab #6: Dijkstra’s Shortest-Path Tree
#
# Date: 18-Oct-2022
# Authors:
#           A01745336 Diego Alejandro Balderas Tlahuitzo
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------

WeightedGraph = dict[str, set[tuple[str, float]]]


def dijkstra_spt(
        initial: str,
        graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    """
    It calculates the shortest path from the initial node to all the other
    nodes

    :param initial: str
    :type initial: str
    :param graph: This is the graph that you want to find the shortest path
    tree of
    :type graph: WeightedGraph
    :return: A tuple of two dictionaries. The first dictionary is the shortest
    path from the initial
    node to all the other nodes. The second dictionary is the answer graph.
    """

    # Creating a list of unvisited nodes, a list of visited nodes, a
    # dictionary of distances, and a dictionary of the answer graph.
    unvisited = [x for x in graph.keys()]
    visited = [initial]

    distances: dict[str, tuple[float, str, float]] = (
                          {key: (float('inf'), '', 0) for key in graph.keys()})
    distances[initial] = (0, '', 0)

    answer_graph: WeightedGraph = {}

    # Calculating the shortest path from the initial node to all the other
    # nodes.
    while len(unvisited) != 0:
        # This is the main part of the algorithm. It is the part that
        # calculates the shortest path from the initial node to all
        # the other nodes.
        current_vertex = min(unvisited, key=lambda x: distances[x][0])

        for neighbor, edge in graph[current_vertex]:

            if neighbor not in visited:
                new_cost = distances[current_vertex][0] + edge

                if new_cost < distances[neighbor][0]:
                    distances[neighbor] = (new_cost, current_vertex, edge)
        unvisited.remove(current_vertex)
        visited.append(current_vertex)

    # This is adding the edges to the answer graph.
    for key, value in distances.items():
        if value[1] != '':
            if answer_graph.get(key) is not None:
                answer_graph[key].add((value[1], value[2]))
            else:
                answer_graph[key] = {(value[1], value[2])}

    # This is adding the edges to the answer graph.
    for key, value in distances.items():
        if value[1] != '':
            if answer_graph.get(value[1]) is not None:
                answer_graph[value[1]].add((key, value[2]))
            else:
                answer_graph[value[1]] = {(key, value[2])}

    return ({key: value[0] for key, value in distances.items()},
            answer_graph)
