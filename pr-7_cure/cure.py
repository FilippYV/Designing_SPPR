import pandas as pd
import matplotlib.pyplot as plt
import math
import random


def generate_data(count):
    # mass_data = []
    # for i in range(count // 4):
    #     mass_data.append([round(random.uniform(0, 2), 2), round(random.uniform(0, 2), 2)])
    #
    # for i in range(count // 4):
    #     mass_data.append([round(random.uniform(0, 2), 2), round(random.uniform(5, 8), 2)])
    #
    # for i in range(count // 4):
    #     mass_data.append([round(random.uniform(5, 7), 2), round(random.uniform(5, 10), 2)])
    #
    # for i in range(count // 4):
    #     mass_data.append([round(random.uniform(9, 10), 2), round(random.uniform(5, 10), 2)])
    #
    # for i in range(count // 4):
    #     mass_data.append([round(random.uniform(2, 3), 2), round(random.uniform(7, 8), 2)])
    #
    # for i in range(count // 4):
    #     mass_data.append([round(random.uniform(3, 3.5), 2), round(random.uniform(7, 8), 2)])
    #
    # for i in range(count // 4):
    #     mass_data.append([round(random.uniform(3, 3.5), 2), round(random.uniform(5, 7), 2)])
    # print(mass_data)
    # mass_data = [[1.93, 1.81], [0.91, 0.03], [1.2, 0.84], [0.47, 1.35], [1.29, 0.39], [1.84, 1.99], [0.32, 0.87],
    #              [0.43, 1.71], [1.76, 0.49], [0.5, 0.54], [0.37, 1.07], [0.79, 0.29], [1.12, 0.74], [0.54, 0.75],
    #              [0.38, 0.33], [1.64, 1.22], [1.95, 0.45], [0.88, 6.61], [1.84, 6.19], [0.55, 7.68], [0.2, 7.35],
    #              [0.74, 6.71], [1.04, 7.72], [1.3, 5.87], [0.46, 7.37], [0.94, 7.83], [0.4, 6.54], [0.13, 5.16],
    #              [1.66, 6.65], [1.04, 5.74], [1.33, 5.15], [0.39, 5.94], [1.96, 6.36], [0.08, 5.37], [6.8, 5.72],
    #              [6.75, 8.76], [6.8, 8.53], [6.17, 7.68], [5.0, 5.62], [6.08, 9.08], [6.08, 5.85], [6.36, 7.42],
    #              [6.19, 5.28], [6.53, 6.23], [6.11, 8.47], [5.14, 6.35], [5.5, 5.53], [6.71, 7.92], [6.71, 7.38],
    #              [5.89, 5.14], [5.01, 6.61], [9.37, 8.19], [9.27, 5.57], [9.32, 7.09], [9.03, 8.05], [9.5, 6.11],
    #              [9.88, 8.71], [9.5, 7.22], [9.4, 8.08], [9.06, 8.32], [9.19, 5.78], [9.91, 9.81], [9.35, 8.27],
    #              [9.53, 5.05], [9.77, 9.63], [9.63, 7.38], [9.58, 7.13], [9.44, 5.53], [2.13, 7.34], [2.49, 7.89],
    #              [2.65, 7.74], [2.23, 7.38], [2.34, 7.46], [2.32, 7.28], [2.07, 7.19], [2.13, 7.78], [2.38, 7.11],
    #              [2.25, 7.54], [2.82, 7.43], [2.46, 7.51], [2.12, 7.21], [2.96, 7.22], [2.17, 7.67], [2.71, 7.11],
    #              [2.53, 7.54], [3.24, 7.1], [3.18, 7.25], [3.28, 7.17], [3.46, 7.13], [3.5, 7.94], [3.1, 7.64],
    #              [3.16, 7.15], [3.3, 7.1], [3.46, 7.41], [3.3, 7.32], [3.3, 7.53], [3.39, 7.64], [3.49, 7.44],
    #              [3.3, 7.87], [3.35, 7.01], [3.08, 7.38], [3.47, 7.04], [3.15, 6.84], [3.45, 6.08], [3.41, 6.22],
    #              [3.41, 6.46], [3.08, 5.21], [3.11, 5.16], [3.41, 6.57], [3.18, 6.64], [3.42, 6.37], [3.26, 6.42],
    #              [3.32, 5.0], [3.15, 6.46], [3.24, 5.23], [3.35, 5.13], [3.16, 5.47], [3.41, 6.5], [3.06, 6.65]]
    mass_data = [[9, 6], [0, 7], [7, 5], [9, 8], [1, 8], [9, 3], [0, 8], [8, 1], [0, 2], [3, 7]]

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


def hierarchy(data):
    massive_path = []
    for i in range(len(data)):
        massive_path.append(i)
    count_group = 6
    while len(set(massive_path)) > count_group:
        minimum_count = 1000000
        minimum_index = 0
        for i, i_i in enumerate(data):
            for j, j_j in enumerate(data):
                if i != j and massive_path[i] != massive_path[j]:
                    long = math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2)
                    if long < minimum_count:
                        minimum_count = long
                        minimum_index = [i, j]
        if massive_path[minimum_index[0]] > massive_path[minimum_index[1]]:
            massive_path[minimum_index[0]] = massive_path[minimum_index[1]]
        else:
            massive_path[minimum_index[1]] = massive_path[minimum_index[0]]
        print(minimum_index)
        # minimum_count = math.sqrt((data[minimum_index[0]][0] - data[minimum_index[1]][0]) ** 2 + (data[minimum_index[0]][1] - data[minimum_index[1]][1]) ** 2)
        print(f' {minimum_count} = math.sqrt(({data[minimum_index[0]][0]} - {data[minimum_index[1]][0]}) ** 2 + ({data[minimum_index[0]][1]} - {data[minimum_index[1]][1]}) ** 2)')
    print()
    print('massive_path')
    print('massive_path')
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(count_group):
        if i not in massive_path:
            max = 100
            for j in massive_path:
                if j > i and j < max:
                    max = j
            for j in range(len(massive_path)):
                if massive_path[j] == max:
                    massive_path[j] = i
    for i in massive_path:
        print(i)
    graph_hierarchy(data, massive_path)
    return massive_path


def graph_hierarchy(data, massive_path_):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    colors = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
              '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    for i in range(len(data)):
        axis.scatter(data[i][0], data[i][1], color=colors[massive_path_[i]])

    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_hierarchy.png')
    fig.clear()


def cure(data, massive_path):
    central_cluster = []
    central_point(central_cluster)

def graph_c(data, central_cluster, massive_path):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    colors = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
              '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    for i in range(len(data)):
        axis.scatter(data[i][0], data[i][1], color=colors[massive_path[i]])

    for j in central_cluster:
        axis.scatter(data[j][0], data[j][1], color='red', s=100)

    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_c.png')
    fig.clear()


def graph_c_counter(data, central_cluster, mass_to_splete, mass_cluster_contour):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    colors = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
              '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    for i in range(len(data)):
        axis.scatter(data[i][0], data[i][1], color=colors[massive_path[i]])

    for j in central_cluster:
        axis.scatter(data[j][0], data[j][1], color='red', s=100)

    for j in mass_to_splete:
        axis.scatter(data[j[0]][0], data[j[1]][1], color='y', s=100)

    print(mass_cluster_contour, '-------------')
    for i in mass_cluster_contour:
        for j in i:
            axis.scatter(data[j][0], data[j][1], color='blue', s=25)

    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_c_contur.png')
    fig.clear()

def central_point(central_cluster):
    central_cluster = []
    cental = list(set(massive_path))
    print(cental, 'central')
    for class_name in cental:
        mass_for_relocation = []
        for index, j in enumerate(data):
            if massive_path[index] == class_name:
                mass_for_relocation.append(index)
        minimum = [1000000, -1]
        for index_i, i in enumerate(mass_for_relocation):
            long = 0
            for index_j, j in enumerate(mass_for_relocation):
                if index_j != index_i:
                    long += math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2)
            if long < minimum[0]:
                minimum = [long, i]
        central_cluster.append(minimum[1])
    print(central_cluster)
    graph_c(data, massive_path, central_cluster)

    mass_cluster_contour = []
    for class_name in cental:
        mass_for_relocation = []
        for index, j in enumerate(data):
            if massive_path[index] == class_name:
                mass_for_relocation.append(index)
        mass_four_point = [central_cluster[class_name]]
        for i in range(4):
            index_max = -1
            max_long = 0
            for index, j in enumerate(mass_for_relocation):
                long = 0
                for k in mass_four_point:
                    if j not in mass_four_point:
                        long += (data[k][0] - data[j][0]) ** 2 + (data[k][1] - data[j][1]) ** 2
                if long > max_long:
                    max_long = long
                    index_max = j
            mass_four_point.append(index_max)
            if i == 0:
                mass_four_point.pop(0)
        print(mass_four_point)
        mass_cluster_contour.append(mass_four_point)

    mass_len_a = []
    for ii, i in enumerate(central_cluster):
        len_a = 0
        for j in mass_cluster_contour[ii]:
            len_a += math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2)
        print(f"({round(len_a,2)} / 4) * 0.75) = {round((len_a / 4) * 0.75,2)})")
        mass_len_a.append((len_a / 4) * 0.50)
    print(mass_len_a, 'lenn_a')
    mass_to_splete = []
    for k, kk in enumerate(mass_cluster_contour):
        for i, ii in enumerate(kk):
            for jj, j in enumerate(data):
                if ii != jj and massive_path[ii] != massive_path[jj] and \
                        mass_len_a[k] > math.sqrt((data[ii][0] - data[jj][0]) ** 2 + (data[ii][1] - data[jj][1]) ** 2):
                    print(ii, jj, massive_path[ii], massive_path[jj], data[ii], data[jj])
                    print(math.sqrt((data[ii][0] - data[jj][0]) ** 2 + (data[ii][1] - data[jj][1]) ** 2))
                    mass_to_splete.append([massive_path[ii], massive_path[jj]])

    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    colors = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
              '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    for i in range(len(data)):
        axis.scatter(data[i][0], data[i][1], color=colors[massive_path[i]])

    for j in central_cluster:
        axis.scatter(data[j][0], data[j][1], color='red', s=25)

    print(mass_cluster_contour, '-------------')
    for i in mass_cluster_contour:
        for j in i:
            axis.scatter(data[j][0], data[j][1], color='blue', s=25)

    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_c.png')
    fig.clear()

    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    colors = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
              '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    for i in range(len(data)):
        axis.scatter(data[i][0], data[i][1], color=colors[massive_path[i]])

    for j in central_cluster:
        axis.scatter(data[j][0], data[j][1], color='red', s=25)

    for j in mass_to_splete:
        axis.scatter(data[j[0]][0], data[j[1]][1], color='y', s=100)

    print(mass_cluster_contour, '-------------')
    for i in mass_cluster_contour:
        for j in i:
            axis.scatter(data[j][0], data[j][1], color='blue', s=25)

    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_c_contur.png')
    fig.clear()


    count_merge_ = 1
    print('-----------')
    print(mass_to_splete)
    print(massive_path)
    if mass_to_splete != 0:
        for k in range(len(mass_to_splete)):
            for i in range(len(massive_path)):
                if massive_path[i] == mass_to_splete[k][1]:
                    massive_path[i] = mass_to_splete[k][0]
        # for k, kk in enumerate(mass_to_splete):
        #     for i, ii in enumerate(massive_path):
        #         if ii == kk[1]:
        #             massive_path[i] = kk[0]
    print(massive_path)

    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    colors = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
              '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    for i in range(len(data)):
        axis.scatter(data[i][0], data[i][1], color=colors[massive_path[i]])
    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_c_end.png')
    fig.clear()


def graph_c(data, massive_path, central_cluster):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    colors = ['#000000', '#808080', '#FF00FF', '#32CD32', '#800000',
              '#FFFF00', '#808000', '#00FF00', '#008000', '#0000FF']
    for i in range(len(data)):
        axis.scatter(data[i][0], data[i][1], color=colors[massive_path[i]])
    for j in central_cluster:
        axis.scatter(data[j][0], data[j][1], color='red', s=100)
    plt.title('График данных')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.savefig('static//start_graph_c.png')
    fig.clear()


if __name__ == '__main__':
    count_point = 70
    data = generate_data(count_point)
    start_graph(data)
    massive_path = hierarchy(data)
    cure(data, massive_path)
