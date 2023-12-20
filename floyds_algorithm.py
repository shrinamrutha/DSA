import networkx as nx
import matplotlib.pyplot as plt
infinity = float("inf")
def make_graph():
    return {
        1: [(-2, 3)],
        2: [(4, 1), (3, 3)],
        3: [(2, 4)],
        4: [(-1, 2)],
    }
def floyd_warshall(G):
    size = len(G)
    matrix = [[infinity] * size for _ in range(size)]
    for i in range(size):
        matrix[i][i] = 0
    for node, edges in G.items():
        for edge in edges:
            cost = edge[0]
            to_node = edge[1]
            matrix[node-1][to_node-1] = cost
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix
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
def make_adjacency_matrix(G):
    size = len(G)
    matrix = [[infinity] * size for _ in range(size)]
    for node, edges in G.items():
        for edge in edges:
            cost, to_node = edge
            matrix[node-1][to_node-1] = cost
    return matrix
def print_adjacency_matrix(adjacency_matrix):
    print('Adjacency matrix:\n')
    for row in adjacency_matrix:
        print(row)
def main():
    G = make_graph()
    plot_weighted_graph(G)
    shortest_path_matrix = floyd_warshall(G)
    print('\nShortest path matrix:\n')
    for item in shortest_path_matrix:
        print(item)
    adjacency_matrix = make_adjacency_matrix(G)
    print_adjacency_matrix(adjacency_matrix)

main()
