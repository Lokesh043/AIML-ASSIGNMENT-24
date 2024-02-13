# Weighted graph represented as an adjacency list
graph = {
    0: [(1, 2), (2, 4)],
        1: [(2, 1), (3, 7)],
            2: [(3, 3), (4, 2)],
                3: [(4, 5), (5, 6)],
                    4: [(5, 3)],
                        5: []
                        }

                        def dijkstra(graph, start, end):
                            # Initialize distances and visited nodes
                                distances = {node: float('inf') for node in graph}
                                    distances[start] = 0
                                        visited = set()

                                            while len(visited) < len(graph):
                                                    # Find the node with the minimum distance
                                                            current_node = min((node for node in graph if node not in visited), key=distances.get)
                                                                    visited.add(current_node)

                                                                            # Update distances for neighboring nodes
                                                                                    for neighbor, weight in graph[current_node]:
                                                                                                if distances[current_node] + weight < distances[neighbor]:
                                                                                                                distances[neighbor] = distances[current_node] + weight

                                                                                                                    return distances[end]

                                                                                                                    shortest_path_cost = dijkstra(graph, 0, 5)
                                                                                                                    print(f"Shortest cost path from node 0 to node 5: {shortest_path_cost}")