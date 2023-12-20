import networkx as nx
import matplotlib.pyplot as plt

infinity = float("inf")

def make_graph():
    return {
        'S': [(8, 'E'), (10, 'A')],
        'A': [(2, 'C')],
        'B': [(1, 'A')],
        'C': [(-2, 'B')],
        'D': [(-4, 'A'), (-1, 'C')],
        'E': [(1, 'D')],
    }

def bellman_ford(G, start):
    shortest_paths = {}
    for node in G:
        shortest_paths[node] = infinity
    shortest_paths[start] = 0
    size = len(G)
    for _ in range(size - 1):
        for node in G:
            for edge in G[node]:
                cost = edge[0]
                to_node = edge[1]
                if shortest_paths[node] + cost < shortest_paths[to_node]:
                    shortest_paths[to_node] = shortest_paths[node] + cost
    return shortest_paths

def plot_weighted_graph(G):
    graph = nx.DiGraph()
    for node, edges in G.items():
        for edge in edges:
            target_node, weight = edge[1], edge[0]
            graph.add_edge(node, target_node, weight=weight)

    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title("Weighted Graph Plot")
    plt.show()

def main():
    start = 'S'

    G = make_graph()
    shortest_paths = bellman_ford(G, start)
    print(f'Shortest path from {start}: {shortest_paths}')

    plot_weighted_graph(G)

main()
