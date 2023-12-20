import networkx as nx
import matplotlib.pyplot as plt
def dfs(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)

    while stack:
        current_node = stack.pop()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
def plot_graph(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
    plt.title("Graph for DFS")
    plt.show()
def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['E'],
        'C': ['F'],
        'D': ['B'],
        'E': ['D'],
        'F': []
    }
    start_node = 'A'
    print("DFS starting from node", start_node)
    dfs(graph, start_node)
    plot_graph(graph)
if __name__ == "__main__":
    main()
