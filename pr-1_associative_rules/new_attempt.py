# import itertools
#
#
# def generate_data():
#     data = []
#     for i in range(10):
#         data.append(i)
#     return data
#
#
# def out_data(data):
#     print('-' * 50)
#     for i in range(len(data)):
#         print(f'Элемент {i} = {data[i]}')
#     print('-' * 50)
#
#
# def generate_combinations(data, count_comb):
#     all_comb = []
#     for count_item in range(1, 5):
#         permutation = itertools.permutations(data, count_item)
#         comb_not_sort = []
#         for comb in permutation:
#             print(list(comb))
#             comb_not_sort.append(list(comb))
#         all_comb.append(comb_not_sort)
#     print('=' * 50)
#     comb_to_item = []
#     permutation = itertools.permutations([0, 1, 2, 3], 4)
#     for i in permutation:
#         comb_to_item.append(list(i))
#     return comb_to_item, all_comb
#
#
# def generate_data_to_sort(comb_indexes, all_comb):
#     all_data_comb = []
#     for mass_comb_item in comb_indexes:
#         mass_index_1 = mass_comb_item[0]
#         mass_index_2 = mass_comb_item[1]
#         for mass_1 in range(len(all_comb[mass_index_1])):
#             for mass_2 in range(len(all_comb[mass_index_2])):
#                 all_data_comb.append([all_comb[mass_index_1][mass_1], all_comb[mass_index_2][mass_2]])
#     print(len(all_data_comb))
#     print(all_data_comb)


import itertools
import time
import pandas as pd
import numpy as np

if __name__ == '__main__':

    data = pd.read_csv('static/data/new_data.csv')

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

    all_comb = []
    for count_item in range(1, 5):
        permutation = itertools.permutations(unique_products, count_item)
        for comb in permutation:
            all_comb.append(list(comb))
    print(len(all_comb))
    mass_group_products = []
    mass_group_products_str = []
    count = 1
    start_time = time.time()
    for i in range(len(all_comb)):
        for j in range(len(all_comb)):
            if i != j and set(all_comb[j]).isdisjoint(all_comb[i]) and set(all_comb[i]).isdisjoint(all_comb[j]):
                if sum([all_comb[i], all_comb[j]], []) not in mass_group_products_str:
                    mass_group_products_str.append(sum([all_comb[i], all_comb[j]], []))
                    mass_group_products.append([all_comb[i], all_comb[j]])
    print("Время = %s seconds" % (time.time() - start_time))
    print(f"Получено сочетаний {len(mass_group_products)}")
    print('\n' * 1)
    print(len(mass_group_products))
