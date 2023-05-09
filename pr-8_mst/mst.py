import random


def generate_start_graph(count):
    graph = []
    for i in range(count - 1):
        for j in range(i + 1, count):
            graph.append([i, j, random.randint(10, 50)])
    print('Начальный граф:')
    for i in graph:
        print(f'{i[0]}, {i[1]}, {i[2]}')
    print()
    return graph


def output_start_graph(graph):
    pass


if __name__ == '__main__':
    count_city = 5
    graph = generate_start_graph(count=count_city)
    output_start_graph(graph)

