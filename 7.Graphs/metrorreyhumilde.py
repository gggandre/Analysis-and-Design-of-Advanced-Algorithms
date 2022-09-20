from typing import Optional
from graph import Graph

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

    # Reuse BFS from Chapter 2 on city_graph
    import sys
    # so we can access the Chapter2 package in the parent directory
    sys.path.insert(0, '..')
    from generic_search import bfs, Node, node_to_path

    bfs_result1: Optional[Node[str]] = bfs(
        "Sendero", lambda x: x == "Exposición", metrorrey.neighbors_for_vertex)
    if bfs_result1 is None:
        print("No solution found using breadth-first search!")
    else:
        path1: list[str] = node_to_path(bfs_result1)
        print("1. Sendero to Exposición:")
        
    sys.path.insert(0, '..')
    from generic_search import bfs, Node, node_to_path
    print(path1)

    bfs_result2: Optional[Node[str]] = bfs(
        "Talleres", lambda x: x == "Hospital Metropolitano", metrorrey.neighbors_for_vertex)
    if bfs_result2 is None:
        print("No solution found using breadth-first search!")
    else:
        path2: list[str] = node_to_path(bfs_result2)
        print("2. Talleres to Hospital Metropolitano:")
    print(path2)
        
    bfs_result3: Optional[Node[str]] = bfs(
        "Alameda", lambda x: x == "Colonia Obrera", metrorrey.neighbors_for_vertex)
    if bfs_result3 is None:
        print("No solution found using breadth-first search!")
    else:
        path3: list[str] = node_to_path(bfs_result3)
        print("3. Alameda to Colonia Obrera:")
    print(path3)

    bfs_result4: Optional[Node[str]] = bfs(
        "Universidad", lambda x: x == "Santa Lucía", metrorrey.neighbors_for_vertex)
    if bfs_result4 is None:
        print("No solution found using breadth-first search!")
    else:
        path4: list[str] = node_to_path(bfs_result4)
        print("4. Universidad to Santa Lucía:")
    print(path4)

    bfs_result5: Optional[Node[str]] = bfs(
        "General I. Zaragoza", lambda x: x == "Del Golfo", metrorrey.neighbors_for_vertex)
    if bfs_result5 is None:
        print("No solution found using breadth-first search!")
    else:
        path5: list[str] = node_to_path(bfs_result5)
        print("5. From General I Zaragoza to Del Golfo:")
    print(path5)

    bfs_result6: Optional[Node[str]] = bfs(
        "Lerdo de Tejada", lambda x: x == "Padre Mier", metrorrey.neighbors_for_vertex)
    if bfs_result6 is None:
        print("No solution found using breadth-first search!")
    else:
        path6: list[str] = node_to_path(bfs_result6)
        print("6. From Lerdo de Tejada to Padre Mier:")
    print(path6)
