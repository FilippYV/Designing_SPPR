import pandas as pd
import matplotlib.pyplot as plt
import math
import random


def generate_data(count):
    mass_data = []
    for i in range(count):
        mass_data.append([random.randrange(0, 10), random.randrange(0, 10)])
    print(mass_data)
    # mass_data = [[2, 9], [8, 2], [5, 6], [7, 5], [8, 2], [1, 5], [4, 5],
    #              [9, 0], [1, 4], [4, 1], [2, 4], [7, 1], [3, 7], [1, 6], [0, 8]]
    # mass_data = [[7, 4], [1, 9], [3, 1], [3, 6], [8, 2], [8, 7], [4, 0], [2, 3],
    #              [0, 7], [0, 7], [6, 9], [1, 8], [1, 6], [3, 0], [4, 5]]
    return mass_data


def start_graph(mass):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for i in mass:
        axis.scatter(i[0], i[1], color='black')
    plt.title('График изначальных данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph.png')
    fig.clear()
    plt.close(fig)


def generate_path(data, cluster_count):
    massive_path = []
    for i in range(len(data)):
        massive_copy_path = []
        for l in range(cluster_count):
            minimum_count = 1000000
            minimum_index = 0
            for j in range(len(data)):
                if i != j and [i, j] not in massive_copy_path and [j, i] not in massive_copy_path:
                    long = math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2)
                    if long < minimum_count:
                        minimum_count = long
                        minimum_index = [i, j]
            print(minimum_count)
            print(minimum_index)
            massive_copy_path.append(minimum_index)
            mass_x = [data[minimum_index[0]][0], data[minimum_index[1]][0]]
            mass_y = [data[minimum_index[0]][1], data[minimum_index[1]][1]]
            massive_path.append([mass_x, mass_y])
    graph_k(data, massive_path)

def graph_k(data, massive_path):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for k in data:
        axis.scatter(k[0], k[1], color='black')
    for i in massive_path:
        plt.plot(i[0], i[1], color='red')

    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_k.png')
    fig.clear()

if __name__ == '__main__':
    count_point = 25
    data = generate_data(count_point)
    start_graph(data)
    cluster_count = 3
    generate_path(data, cluster_count)
