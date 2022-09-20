from typing import Optional
from graph import Graph


def graph_solution(w, z):
    import sys

    sys.path.insert(0, '..')
    from generic_search import bfs, Node, node_to_path

    bfs_result: Optional[Node[str]] = bfs(
        w, lambda x: x == z, metrorrey.neighbors_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: list[str] = node_to_path(bfs_result)
        print(f'Path from {w} to {z}: ')
        print(path)


if __name__ == '__main__':
    metrorrey: Graph[str] = Graph(['Talleres',
                                   'San Bernabé',
                                   'Unidad Modelo',
                                   'Aztlán',
                                   'Peniteniana',
                                   'Alfonso Reyes',
                                   'Mitras',
                                   'Simón Bolívar',
                                   'Hospital',
                                   'Edison',
                                   'Central',
                                   'Cuauhtémoc',
                                   'Del Golfo',
                                   'Félix U. Gómez',
                                   'Parque Fundidora',
                                   'Y Griega',
                                   'Eloy Cavazos',
                                   'Lerdo de Tejada',
                                   'Exposición',
                                   'Sendero',
                                   'Santiago Tapia',
                                   'San Nicolás',
                                   'Anáhuac',
                                   'Universidad',
                                   'Niños Héroes',
                                   'Regina',
                                   'General Anaya',
                                   'Alameda',
                                   'Fundadores',
                                   'Padre Mier',
                                   'General I. Zaragoza',
                                   'Santa Lucía',
                                   'Colonia Obrera',
                                   'Metalúrgicos',
                                   'Colonia Moderna',
                                   'Ruiz Cortines',
                                   'Los Ángeles',
                                   'Hospital Metropolitano'])

    metrorrey.add_edge_by_vertices('Talleres', 'San Bernabé')
    metrorrey.add_edge_by_vertices('San Bernabé', 'Unidad Modelo')
    metrorrey.add_edge_by_vertices('Unidad Modelo', 'Aztlán')
    metrorrey.add_edge_by_vertices('Aztlán', 'Peniteniana')
    metrorrey.add_edge_by_vertices('Peniteniana', 'Alfonso Reyes')
    metrorrey.add_edge_by_vertices('Alfonso Reyes', 'Mitras')
    metrorrey.add_edge_by_vertices('Mitras', 'Simón Bolívar')
    metrorrey.add_edge_by_vertices('Simón Bolívar', 'Hospital')
    metrorrey.add_edge_by_vertices('Hospital', 'Edison')
    metrorrey.add_edge_by_vertices('Edison', 'Central')
    metrorrey.add_edge_by_vertices('Central', 'Cuauhtémoc')
    metrorrey.add_edge_by_vertices('Cuauhtémoc', 'Del Golfo')
    metrorrey.add_edge_by_vertices('Del Golfo', 'Félix U. Gómez')
    metrorrey.add_edge_by_vertices('Félix U. Gómez', 'Parque Fundidora')
    metrorrey.add_edge_by_vertices('Parque Fundidora', 'Y Griega')
    metrorrey.add_edge_by_vertices('Y Griega', 'Eloy Cavazos')
    metrorrey.add_edge_by_vertices('Eloy Cavazos', 'Lerdo de Tejada')
    metrorrey.add_edge_by_vertices('Lerdo de Tejada', 'Exposición')
    metrorrey.add_edge_by_vertices('Sendero', 'Santiago Tapia')
    metrorrey.add_edge_by_vertices('Santiago Tapia', 'San Nicolás')
    metrorrey.add_edge_by_vertices('San Nicolás', 'Anáhuac')
    metrorrey.add_edge_by_vertices('Anáhuac', 'Universidad')
    metrorrey.add_edge_by_vertices('Universidad', 'Niños Héroes')
    metrorrey.add_edge_by_vertices('Niños Héroes', 'Regina')
    metrorrey.add_edge_by_vertices('Regina', 'General Anaya')
    metrorrey.add_edge_by_vertices('General Anaya', 'Cuauhtémoc')
    metrorrey.add_edge_by_vertices('Cuauhtémoc', 'Alameda')
    metrorrey.add_edge_by_vertices('Alameda', 'Fundadores')
    metrorrey.add_edge_by_vertices('Fundadores', 'Padre Mier')
    metrorrey.add_edge_by_vertices('Padre Mier', 'General I. Zaragoza')
    metrorrey.add_edge_by_vertices('General I. Zaragoza', 'Santa Lucía')
    metrorrey.add_edge_by_vertices('Santa Lucía', 'Colonia Obrera')
    metrorrey.add_edge_by_vertices('Colonia Obrera', 'Félix U. Gómez')
    metrorrey.add_edge_by_vertices('Félix U. Gómez', 'Metalúrgicos')
    metrorrey.add_edge_by_vertices('Metalúrgicos', 'Colonia Moderna')
    metrorrey.add_edge_by_vertices('Colonia Moderna', 'Ruiz Cortines')
    metrorrey.add_edge_by_vertices('Ruiz Cortines', 'Los Ángeles')
    metrorrey.add_edge_by_vertices('Los Ángeles', 'Hospital Metropolitano')
    graph_solution('Sendero', 'Exposición')
    print()
    graph_solution('Talleres', 'Hospital Metropolitano')
    print()
    graph_solution('Alameda', 'Colonia Obrera')
    print()
    graph_solution('Universidad', 'Santa Lucía')
    print()
    graph_solution('General I. Zaragoza', 'Del Golfo')
    print()
    graph_solution('Lerdo de Tejada', 'Padre Mier')
    print()
