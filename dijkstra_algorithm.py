import networkx as nx
import matplotlib.pyplot as plt

infinity = float("inf")

def make_weighted_graph():
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    }

def dijkstras(G, start='A'):
    shortest_paths = {}
    unvisited = list(G.keys())
    for node in unvisited:
        shortest_paths[node] = infinity
    shortest_paths[start] = 0
    while unvisited:
        min_node = None
        for node in unvisited:
            if min_node is None:
                min_node = node
            elif shortest_paths[node] < shortest_paths[min_node]:
                min_node = node
        for edge in G[min_node]:
            cost = edge[0]
            to_node = edge[1]
            if cost + shortest_paths[min_node] < shortest_paths[to_node]:
                shortest_paths[to_node] = cost + shortest_paths[min_node]
        unvisited.remove(min_node)
    return shortest_paths

def plot_weighted_graph(G):
    graph = nx.Graph()
    for node, edges in G.items():
        for edge in edges:
            target_node, weight = edge[1], edge[0]
            graph.add_edge(node, target_node, weight=weight)

    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

def main():
    G = make_weighted_graph()
    start = 'A'
    shortest_paths = dijkstras(G, start)
    print(f'Shortest path from {start}: {shortest_paths}')

    plot_weighted_graph(G)

main()
