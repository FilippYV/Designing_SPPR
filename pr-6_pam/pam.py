import matplotlib.pyplot as plt
import math
import random


def generate_data(count_point):
    mass_data = []
    for i in range(count_point):
        mass_data.append([random.randrange(0, 10), random.randrange(0, 10)])
    print(mass_data, "\n")
    # x = [5.26, 8.4, 3.59, 7.06, 8.42, 3.09, 9.09, 1.74, 6.34, 6.45]
    # y = [9.06, 0.0, 7.28, 9.06, 1.41, 9.85, 1.0, 1.0, 5.0, 3.0]
    # for i in range(len(x)):
    #     mass_data.append([x[i], y[i]])
    # mass_data = [[9, 6], [0, 7], [7, 5], [9, 8], [1, 8], [9, 3], [0, 8], [8, 1], [0, 2], [3, 7]]
    # for i in mass_data:
    #     print(i[1])
    print()
    return mass_data


def start_graph(mass):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for i in mass:
        axis.scatter(i[0], i[1], color='black')
    plt.xlim([-1, 11])
    plt.ylim([-1, 11])
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
    plt.xlim([-1, 11])
    plt.ylim([-1, 11])
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
    plt.xlim([-1, 11])
    plt.ylim([-1, 11])
    plt.savefig(f'static/elbow_method./{k}_point_cluster.png')
    fig.clear()
    plt.close(fig)


def graph_elbow_long(mass_elbow_length):
    fig = plt.figure(figsize=(10, 7))
    mass_k = []
    for i in range(len(mass_elbow_length)):
        mass_k.append(i + 1)
    print(mass_k)
    print(mass_elbow_length)
    plt.bar(mass_k, mass_elbow_length)
    plt.title('График правила локтя')
    plt.ylabel('Евклидово расстояние')
    plt.xlabel('Количество вершин')
    plt.savefig(f'static./elbow_long.png')
    fig.clear()
    plt.close(fig)


def distribution_of_points_by_clusters(mass_to_clusters, mass, central_points):  # распределение точек по кластерам
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
    # print()
    # for i in mass_to_clusters:
    #     if i == 0:
    #         print(1)
    #     elif i == 1:
    #         print(2)
    # print('_________')


def redefining_cluster_centers(central_points, mass, mass_to_clusters):  # переопределение центров
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


def calculation_of_long_elbows(central_points, mass, mass_to_clusters):
    elbow_length = 0
    for class_name in range(len(central_points)):
        mass_for_relocation = []
        for index, j in enumerate(mass):
            if mass_to_clusters[index] == class_name:
                mass_for_relocation.append(index)
        index_i = central_points[class_name]
        for index_j, j in enumerate(mass_for_relocation):
            if mass_to_clusters[index_j] == class_name:
                elbow_length += math.sqrt(
                    (mass[index_i][0] - mass[j][0]) ** 2 + (mass[index_i][1] - mass[j][1]) ** 2)
    return elbow_length


def generate_start_point(central_points, mass):
    minimum = [0, 0]
    # table = []
    for i, element in enumerate(mass):
        long = 0
        for j in range(len(mass)):
            long += math.sqrt((element[0] - mass[j][0]) ** 2 + (element[1] - mass[j][1]) ** 2)
        if long > minimum[0]:
            minimum = [long, i]
        # table.append(round(long,2))
    central_points.append(minimum[1])


def elbow_method(mass):
    color = ['#000000', '#808080', '#FF00FF', '#32CD32',
             '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    minimum = 1
    maximum = 5
    mass_elbow_length = []
    start_point = random.randint(0, len(mass) - 1)
    # central_points = []  # начальная точка
    # generate_start_point(central_points, mass)
    for k in range(minimum, maximum + 1):
        central_points = [random.randint(0, len(mass)-1)]  # начальная точка
        cluster_center_definitions(k, central_points, mass)  # опеределения центра кластеров
        graph_for_elbow_method(mass, central_points, k)
        mass_to_clusters = []
        distribution_of_points_by_clusters(mass_to_clusters, mass, central_points)  # распределение точек по кластерам
        redefining_cluster_centers(central_points, mass, mass_to_clusters)  # переопределение центров
        graph_for_elbow_method_cluster(mass, central_points, k, color, mass_to_clusters)
        elbow_length = calculation_of_long_elbows(central_points, mass, mass_to_clusters)

        mass_elbow_length.append(elbow_length)
        graph_elbow_long(mass_elbow_length)
    for index, i in enumerate(mass_elbow_length):
        print(f'Если количество элементов = {index + 1}, то\n'
              f'Евклидово расстояние по правилу локтя = {i}\n')


def cluster_center_definitions(k, central_points, mass):  # опеределения центра кластеров
    if k != 1:  # для метода локтя
        for n in range(k - 1):
            minimum = [0, 0]
            # table = []
            for i, element in enumerate(mass):
                if i not in central_points:
                    long = 0
                    for j in central_points:
                        long += math.sqrt((element[0] - mass[j][0]) ** 2 + (element[1] - mass[j][1]) ** 2)
                    if long > minimum[0]:
                        minimum = [long, i]
                    # table.append(round(long,2))
            central_points.append(minimum[1])
    # else:
    #     minimum = [0, 0]
    #     # table = []
    #     for i, element in enumerate(mass):
    #         long = 0
    #         for j in range(len(mass)):
    #             long += math.sqrt((element[0] - mass[j][0]) ** 2 + (element[1] - mass[j][1]) ** 2)
    #         if long > minimum[0]:
    #             minimum = [long, i]
    #         # table.append(round(long,2))
    #     central_points.append(minimum[1])
        # for i in table:
        #     print(str(i).replace('.', ','))
        # new_table = []
        # for i in range(0, 9):
        #     new_table.append(math.sqrt((mass[i][0] - mass[9][0]) ** 2 + (mass[i][1] - mass[9][1]) ** 2))
        # for i in new_table:
        #     print(str(round(i, 2)).replace('.', ','))


def centroid(mass):
    color = ['#000000', '#808080', '#FF00FF', '#32CD32',
             '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    start_point = random.randint(0, len(mass) - 1)
    central_points = [start_point]  # начальная точка
    k = int(input('Введите число кластеров: '))
    cluster_center_definitions(k, central_points, mass)
    graph_for_elbow_method(mass, central_points, k)
    mass_to_clusters = []
    distribution_of_points_by_clusters(mass_to_clusters, mass, central_points)
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
    graph_centroid(mass, central_points, k, color, mass_to_clusters)


def graph_centroid(mass, central_points, k, color, mass_to_clusters):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for index, i in enumerate(mass):
        axis.scatter(i[0], i[1], color=color[mass_to_clusters[index]], s=100)
    for i in central_points:
        axis.scatter(mass[i][0], mass[i][1], color='red', s=25)
    plt.title(f'График для {k} кластеров')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.xlim([-1, 11])
    plt.ylim([-1, 11])
    plt.savefig(f'static//pam_centroid.png')
    fig.clear()
    plt.close(fig)


if __name__ == '__main__':
    count_point = 20
    data = generate_data(count_point)
    start_graph(data)
    elbow_method(data)
    centroid(data)
