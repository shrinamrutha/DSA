import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph):
    mst_edges = set()
    start_node = list(graph.keys())[0]
    visited_nodes = {start_node}
    heap = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node].items()]
    heapq.heapify(heap)

    while heap:
        weight, current_node, next_node = heapq.heappop(heap)

        if next_node not in visited_nodes:
            visited_nodes.add(next_node)
            mst_edges.add((current_node, next_node, weight))

            for neighbor, weight in graph[next_node].items():
                if neighbor not in visited_nodes:
                    heapq.heappush(heap, (weight, next_node, neighbor))

    return mst_edges

def plot_graph(graph, edges, title="Graph"):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.show()

def main():
    graph = {
        'A': {'B': 2, 'D': 7},
        'B': {'A': 2, 'D': 8, 'C': 5, 'E': 7},
        'C': {'B': 5, 'E': 1},
        'D': {'A': 7, 'B': 8, 'E': 4},
        'E': {'B': 7, 'C': 1, 'D': 4}
    }

    mst_edges = prim(graph)
    print("Minimum Spanning Tree Edges:", mst_edges)

    plot_graph(graph, mst_edges, title="Minimum Spanning Tree")

if __name__ == "__main__":
    main()
