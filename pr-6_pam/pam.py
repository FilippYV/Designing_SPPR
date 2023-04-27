import pandas as pd
import matplotlib.pyplot as plt
import math
import random


def generate_data(count_point):
    mass_data = []
    for i in range(count_point):
        mass_data.append([random.randrange(0, 10), random.randrange(0, 10)])
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


def graph_for_elbow_method(mass, central_points, k):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for i in mass:
        axis.scatter(i[0], i[1], color='black')
    for i in central_points:
        axis.scatter(mass[i][0], mass[i][1], color='red', s=100)
    plt.title('График изначальных данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig(f'static/elbow_method./{k}_point.png')
    fig.clear()
    plt.close(fig)


def graph_for_elbow_method_cluster(mass, central_points, k, color, mass_to_clusters):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for index, i in enumerate(mass):
        axis.scatter(i[0], i[1], color=color[mass_to_clusters[index]])
    for i in central_points:
        axis.scatter(mass[i][0], mass[i][1], color='red', s=100)
    plt.title('График изначальных данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig(f'static/elbow_method./{k}_point_cluster.png')
    fig.clear()
    plt.close(fig)


def graph_elbow_long(mass_elbow_length):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for index, i in enumerate(mass_elbow_length):
        axis.scatter(index + 1, i, color='red')
    plt.plot(range(1, len(mass_elbow_length) + 1), mass_elbow_length, color='blue')
    plt.title('График правила локтя')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig(f'static./elbow_long.png')
    fig.clear()
    plt.close(fig)


def elbow_method(mass):
    color = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
             '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    minimum = 1
    maximum = 5
    mass_elbow_length = []
    start_point = random.randint(0, len(mass) - 1)
    for k in range(minimum, maximum + 1):
        central_points = [start_point]  # начальная точка
        if k != 1:  # для метода локтя
            for n in range(k - 1):
                minimum = [0, 0]
                for i, element in enumerate(mass):
                    if i not in central_points:
                        long = 0
                        for j in central_points:
                            long += math.sqrt((element[0] - mass[j][0]) ** 2 + (element[1] - mass[j][1]) ** 2)
                        if long > minimum[0]:
                            minimum = [long, i]
                central_points.append(minimum[1])
                print(minimum)
        graph_for_elbow_method(mass, central_points, k)
        mass_to_clusters = []
        for i, element in enumerate(mass):
            minimum = [1000000, 0]
            if i not in central_points:
                for index, j in enumerate(central_points):
                    long = math.sqrt((element[0] - mass[j][0]) ** 2 + (element[1] - mass[j][1]) ** 2)
                    if long < minimum[0]:
                        minimum = [long, index]
                mass_to_clusters.append(minimum[1])
            else:
                for index, j in enumerate(central_points):
                    if element[0] == mass[j][0] and element[1] == mass[j][1]:
                        mass_to_clusters.append(index)
        # выбор центральный точки
        for class_name in range(len(central_points)):
            mass_for_relocation = []
            for index, j in enumerate(mass):
                if mass_to_clusters[index] == class_name:
                    mass_for_relocation.append(index)
            minimum = [1000000, 0]
            for index_i, i in enumerate(mass_for_relocation):
                long = 0
                for index_j, j in enumerate(mass_for_relocation):
                    if index_j != index_i:
                        long += math.sqrt((mass[i][0] - mass[j][0]) ** 2 + (mass[i][1] - mass[j][1]) ** 2)
                if long < minimum[0]:
                    minimum = [long, i]
            central_points[class_name] = minimum[1]
        for a in range(3):
            for class_name in range(len(central_points)):
                mass_for_relocation = []
                for index, j in enumerate(mass):
                    if mass_to_clusters[index] == class_name:
                        mass_for_relocation.append(index)
                minimum = [1000000, 0]
                for index_i, i in enumerate(mass_for_relocation):
                    long = 0
                    for index_j, j in enumerate(mass_for_relocation):
                        if index_j != index_i:
                            long += math.sqrt((mass[i][0] - mass[j][0]) ** 2 + (mass[i][1] - mass[j][1]) ** 2)
                    if long < minimum[0]:
                        minimum = [long, i]
                central_points[class_name] = minimum[1]
        graph_for_elbow_method_cluster(mass, central_points, k, color, mass_to_clusters)
        elbow_length = 0
        for class_name in range(len(central_points)):
            mass_for_relocation = []
            for index, j in enumerate(mass):
                if mass_to_clusters[index] == class_name:
                    mass_for_relocation.append(index)
            index_i = central_points[class_name]
            for index_j, j in enumerate(mass_for_relocation):
                if mass_to_clusters[index_j] == class_name:
                    elbow_length += math.sqrt((mass[index_i][0] - mass[j][0]) ** 2 + (mass[index_i][1] - mass[j][1]) ** 2)
        mass_elbow_length.append([elbow_length])
        graph_elbow_long(mass_elbow_length)



if __name__ == '__main__':
    count_point = 50
    data = generate_data(count_point)
    start_graph(data)
    elbow_method(data)
