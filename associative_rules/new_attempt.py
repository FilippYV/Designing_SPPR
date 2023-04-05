import itertools


def generate_data():
    data = []
    for i in range(10):
        data.append(i)
    return data


def out_data(data):
    print('-' * 50)
    for i in range(len(data)):
        print(f'Элемент {i} = {data[i]}')
    print('-' * 50)


def generate_combinations(data, count_comb):
    all_comb = []
    for count_item in range(1, 5):
        permutation = itertools.permutations(data, count_item)
        comb_not_sort = []
        for comb in permutation:
            print(list(comb))
            comb_not_sort.append(list(comb))
        all_comb.append(comb_not_sort)
    print('=' * 50)
    comb_to_item = []
    permutation = itertools.permutations([0, 1, 2, 3], 4)
    for i in permutation:
        comb_to_item.append(list(i))
    return comb_to_item, all_comb


def generate_data_to_sort(comb_indexes, all_comb):
    all_data_comb = []
    for mass_comb_item in comb_indexes:
        mass_index_1 = mass_comb_item[0]
        mass_index_2 = mass_comb_item[1]
        for mass_1 in range(len(all_comb[mass_index_1])):
            for mass_2 in range(len(all_comb[mass_index_2])):
                all_data_comb.append([all_comb[mass_index_1][mass_1], all_comb[mass_index_2][mass_2]])
    print(len(all_data_comb))
    print(all_data_comb)


import itertools
import time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    data = pd.read_csv('static//new_data.csv')

    unique_receipts = data.receipt_number.unique()
    print(len(unique_receipts))

    unique_products = data['product'].unique()
    print(len(unique_products))

    data_np = data.to_numpy()

    group_products_receipts = []
    for i in unique_receipts:
        micro_data = []
        for j in data_np:
            if j[0] == i:
                micro_data.append(j[1])
        group_products_receipts.append(micro_data)

    groups = []
    for count_item in range(1, 5):
        permutation = itertools.permutations(unique_products, count_item)
        pod_g =[]
        for comb in permutation:
            pod_g.append(list(comb))
        groups.append(pod_g)

    print('--------------')
    mass_group_products = [[['x'], ['X']]]
    for x in groups:
        start_time = time.time()
        print(len(x))
        for i in range(len(x)):
            # start_time = time.time()
            # print('Номер', i)
            for j in range(len(x)):
                if i != j and set(x[j]).isdisjoint(x[i]) and set(x[i]).isdisjoint(x[j]):
                    on_off = True
                    for k in mass_group_products:
                        if sum(k, []) == sum([x[j], x[j]], []):
                            on_off = False
                    if on_off:
                        mass_group_products.append([x[i], x[j]])
        print("Время = %s seconds" % (time.time() - start_time))

    print(len(mass_group_products))
    print(mass_group_products[0], mass_group_products[1])

# if __name__ == '__main__':
#     unique_product = generate_data()
#     out_data(unique_product)
#     combination_indexes, all_combinations = generate_combinations(unique_product, 3)
#     generate_data_to_sort(combination_indexes, all_combinations)
