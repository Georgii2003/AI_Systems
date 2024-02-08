import networkx as nx
import random
import time
import matplotlib as plt

# Функция по созданию графа
def create_graph(nodes, edges):
    G = nx.Graph()
    for i in range(nodes):
        G.add_node(i)
    while len(G.edges()) < edges:
        node1 = random.randint(0, nodes-1)
        node2 = random.randint(0, nodes-1)
        if node1 != node2 and not G.has_edge(node1, node2):
            weight = random.randint(1, 10)
            G.add_edge(node1, node2, weight=weight)
    return G

# Функция по расчёту кратчайшего метода
def calculate_shortest_path(G, method):
    start_time = time.time()
    if method == 'Дейкстры':
        shortest_paths = nx.all_pairs_dijkstra_path(G)
    elif method == 'Беллмана-Форда':
        shortest_paths = nx.all_pairs_bellman_ford_path(G)
    elif method == 'Флойда-Уоршелла':
        shortest_paths = nx.floyd_warshall(G)
    else:
        print("Неизвестный метод")
        return
    end_time = time.time()
    print(f"Время используемое алгоритмом {method}: {end_time - start_time} seconds")
    return shortest_paths

graphs = int(input("Введите количество графов: "))
nodes = int(input("Введите количество узлов: "))
edges = int(input("Введите количество рёбер: "))

for i in range(graphs):
    G = create_graph(nodes, edges)
    print(f"Graph {i+1}:")
    nx.draw(G, with_labels=True)
    plt.show()
    for method in ['Дейкстры', 'Беллмана-Форда', 'Флойда-Уоршелла']:
        shortest_paths = calculate_shortest_path(G, method)
        print(f"Кратчайшие пути рассчитываются с помощью алгоритма {method}: {shortest_paths}")