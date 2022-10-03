from typing import Optional
from graph import Graph
from edge import Edge


class graph_cicle(Graph):
    def __init__(self, nodes, edges, is_directed=False):
        super().__init__(nodes, is_directed)
        self.add_multiple_edges(edges)
        self.color = {}
        self.parent = {}
        self.output = []
        self.is_cycle = False

        for node in self.adj_list.keys():
            self.color[node] = "W"
            self.parent[node] = None

    def has_cicle(self, source):
        self.color[source] = "G"
        self.output.append(source)

        for v in self.adj_list[source]:
            if self.color[v] == "W":
                self.parent[v] = source
                cycle = self.has_cicle(v)
                if cycle:
                    self.is_cycle = True
                    return True
            elif self.color[v] == "G" and self.parent[source] != v:
                self.is_cycle = True
                return True
        self.color[source] = "B"
        return False

    def print_cycle_path(self):
        if self.is_cycle:
            return self.output


# edges = [
#     ("A", "B"),
#     ("C", "B"),
#     ("C", "D"),
#     ("D", "E"),
# ]

undirected = [
    ("A", "B"),
    ("A", "D"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E")
]


edges = [
    ("A", "C"),
    ("A", "B"),
    ("B", "D"),
    ("D", "A"),
    ("D", "E"),
]
nodes = ["A", "B", "C", "D", "E"]
undirected = [
    ("A", "B"),
    ("A", "D"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E")
]
dc = graph_cicle(nodes, edges, False)
print(dc.has_cicle("A"))
print(dc.print_cycle_path())