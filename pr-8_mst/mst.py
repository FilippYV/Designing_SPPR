import matplotlib.pyplot as plt
from pyvis.network import Network
import random
import time


def generate_start_graph(count):
    # graph = []
    # for i in range(count - 1):
    #     for j in range(i + 1, count):
    #         graph.append([i, j, random.randint(10, 50)])
    # print('Начальный граф:')
    # for i in graph:
    #     print(f'{i[0]}, {i[1]}, {i[2]}')
    # print()
    graph = [[0, 1, 38], [0, 2, 22], [0, 3, 22], [0, 4, 24], [1, 2, 14], [1, 3, 27], [1, 4, 32], [2, 3, 26], [2, 4, 28],
             [3, 4, 39]]
    return graph


def output_start_graph(graph, count):
    print('Вывод начального графа')
    net = Network()
    for i in range(count):
        net.add_node(i, label=f"{i}")
    for i in graph:
        net.add_edge(i[0], i[1], value=i[2])
    net.save_graph('static//nodes.html')
    print()


def new_iter_graph(massive_visited_cities, count, iteration):
    print(f'Вывод графа для {iteration} итерации')
    net = Network()
    for i in range(count):
        if i not in massive_visited_cities:
            net.add_node(i, label=f"{i}", color='blue')
        else:
            net.add_node(i, label=f"{i}", color='red')
    for i in graph:
        net.add_edge(i[0], i[1], value=i[2])
    net.save_graph(f'static//nodes_{iteration}.html')
    print()


def formation_all_possible_paths(graph, massive_visited_cities, massive_route):
    massive_to_search_min = []
    for i in range(len(graph)):
        if graph[i][0] not in massive_visited_cities and graph[i][1] in massive_visited_cities or \
                graph[i][1] not in massive_visited_cities and graph[i][0] in massive_visited_cities:
            massive_to_search_min.append([graph[i], i])

    minimum_paths = 10000
    paths_index = -1

    for i in range(len(massive_to_search_min)):
        if massive_to_search_min[i][0][2] < minimum_paths:
            paths_index, minimum_paths = massive_to_search_min[i][1], massive_to_search_min[i][0][2]

    if graph[paths_index][0] not in massive_visited_cities:
        massive_visited_cities.append(graph[paths_index][0])
    elif graph[paths_index][1] not in massive_visited_cities:
        massive_visited_cities.append(graph[paths_index][1])
    massive_route.append(paths_index)
    print(massive_visited_cities)

    time.sleep(0.1)


if __name__ == '__main__':
    count_city = 5
    massive_visited_cities = []
    massive_route = []
    graph = generate_start_graph(count=count_city)
    output_start_graph(graph, count_city)
    start_city = int(input(f'Введите начальню точку от 0 до {count_city - 1}: '))
    iteration = 0
    massive_visited_cities.append(start_city)
    new_iter_graph(massive_visited_cities, count_city, iteration)
    iteration += 1
    while len(massive_visited_cities) < count_city:
        formation_all_possible_paths(graph, massive_visited_cities, massive_route)
        new_iter_graph(massive_visited_cities, count_city, iteration)
        iteration += 1
    print()
    print(massive_visited_cities)
    print(massive_route)
