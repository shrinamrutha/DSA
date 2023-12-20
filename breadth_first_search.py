from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def plot_graph(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
    plt.title("Graph Visualization")
    plt.show()
def main():
    graph = {
        'A': ['B','C'],
        'B': [],
        'C': ['D','E'],
        'D': [],
        'E': ['F','G'],
        'F': [],
        'G':['F']
    }
    start_node = 'C'
    print("BFS starting from node", start_node)
    bfs(graph, start_node)
    plot_graph(graph)
if __name__ == "__main__":
    main()
