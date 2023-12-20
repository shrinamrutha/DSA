import networkx as nx
import matplotlib.pyplot as plt
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    def union(self, root1, root2):
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1
def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    edges.sort()
    mst_edges = []
    disjoint_set = DisjointSet(graph.keys())
    for edge in edges:
        weight, u, v = edge
        root1 = disjoint_set.find(u)
        root2 = disjoint_set.find(v)
        if root1 != root2:
            mst_edges.append((u, v, weight))
            disjoint_set.union(root1, root2)
    return mst_edges
def plot_graph(graph, mst_edges, title="Graph with Minimum Spanning Tree"):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.show()
def print_mst(mst_edges):
    print("Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"Edge: {u} - {v}, Weight: {weight}")
graph = {
    'A': [('B', 2), ('D', 7)],
    'B': [('A', 2), ('D', 8), ('C', 5), ('E', 7)],
    'C': [('B', 5), ('E', 1)],
    'D': [('A', 7), ('B', 8), ('E', 4)],
    'E': [('B', 7), ('C', 1), ('D', 4)]
}
minimum_spanning_tree_edges = kruskal(graph)
plot_graph(graph, minimum_spanning_tree_edges)
print_mst(minimum_spanning_tree_edges)