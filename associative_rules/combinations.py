import itertools
import pandas as pd
import numpy as np
import seaborn as sn


def add_x(data):
    massive = []
    for i in data:
        massive.append(i)
    return massive


if __name__ == '__main__':

    data = pd.read_csv('static//new_data.csv')

    unique_products = []
    unique_products = data['product'].unique()
    print(len(unique_products))
    n = len(unique_products)

    unique_receipts = data.receipt_number.unique()
    print(len(unique_receipts), unique_receipts)

    data_np = data.to_numpy()
    group_products_receipts = []
    for i in unique_receipts:
        micro_data = []
        for j in data_np:
            if j[0] == i:
                micro_data.append(j[1])
        group_products_receipts.append(micro_data)

    # mass_to_del = []
    #
    # for item in range(len(group_products_receipts)):
    #     start_massive = []
    #     for i in group_products_receipts[item]:
    #         start_massive.append(i)
    #     unique_change = []
    #     print(f'Создание {item}//{len(group_products_receipts)}')
    #     if len(start_massive) <= 4:
    #         long = len(start_massive)
    #     else:
    #         long = 4
    #     for j in range(1, long):
    #         massive_j = itertools.permutations(start_massive, j)
    #         for k in massive_j:
    #             elem_k = []
    #             for k_el in k:
    #                 elem_k.append(k_el)
    #             # print(type(elem_k[0]), type('s'))
    #             # if type(elem_k[0]) != type('s'):
    #             unique_change.append(elem_k)
    #     print(len(mass_group_products))
    #     # print(mass_group_product)
    #     # exit(123)
    #     for i in range(len(unique_change)):
    #         for j in range(len(unique_change)):
    #             if unique_change[i] != unique_change[j] and set(unique_change[j]).isdisjoint(unique_change[i]) \
    #                     and set(unique_change[i]).isdisjoint(unique_change[j]) and \
    #                     len(set(unique_change[i])) == len(unique_change[i]) and \
    #                     len(set(unique_change[j])) == len(unique_change[j]):
    #                 if [unique_change[i], unique_change[j]] not in mass_group_products:
    #                     mass_group_products.append([unique_change[i], unique_change[j]])
    #                     # print(mass_group_products[-1])
    # # start_index = 0
    # # stop_index = len(mass_group_products)
    # # print('Было', len(mass_group_products))
    # # while start_index != stop_index:
    # #     first = mass_group_products[start_index][0]
    # #     second = mass_group_products[start_index][1]
    # #     count = 0
    # #     number = 0
    # #     for i in range(len(mass_group_products)):
    # #         if mass_group_products[i][0] == first and mass_group_products[i][1] == second or \
    # #                 mass_group_products[i][1] == first and mass_group_products[i][0] == second:
    # #             count += 1
    # #         if count == 2:
    # #             mass_to_del.append([mass_group_products[i][0], mass_group_products[i][1]])
    # #             count -= 1
    # #     start_index += 1
    # # print('Стало', len(mass_group_products))
    # # print('Dell')
    # count = 0
    # new_mass = []
    # for i in mass_group_products:
    #     if i not in new_mass:
    #         new_mass.append(i)

    # print(len(mass_group_products))
    # for i in range(25):
    #     print(mass_group_products[i])
    # for i in massive:
    #     start_item = i
    #     mass = [start_item]
    #     for j in range(1, len(massive) - 1 - len(mass)):
    #         mass.append(massive[j])
    #     for j in massive:
    #         if j not in mass:
    #             mass_group_product.append([mass, [j]])

    # print(mass_group_product)

    # group_products_index = []
    #
    # for i in range(len(group_products_receipts)):
    #     massive = []
    #     for j in range(len(unique_products)):
    #         if unique_products[j] not in group_products_receipts[i]:
    #             massive.append(0)
    #         else:
    #             massive.append(1)
    #     group_products_index.append(massive)
    #
    # group_products = []
    # for i in group_products_index:
    #     massive = []
    #     for j in range(len(i)):
    #         massive.append(i[j])

    # for i in group_products_index:
    #     print(i)
    # mass_group_products = []
    # for i in range(n):
    #     for j in range(n):
    #         if j != i:
    #             mass_group_products.append([[unique_products[i]], [unique_products[j]]])
    #             mass_group_products.append([[unique_products[j]], [unique_products[i]]])
    #
    #             mass_for_two = [unique_products[i], unique_products[j]]
    #             if j <= n - 2:
    #                 for two in unique_products:
    #                     if two not in mass_for_two:
    #                         mass_group_products.append([mass_for_two, [two]])
    #                         for two_two in unique_products:
    #                             if two_two not in mass_for_two and two:
    #                                 mass_group_products.append([[mass_for_two[0], mass_for_two[1]], [two, two_two]])
    #                                 for two_three in unique_products:
    #                                     if two_three not in mass_for_two \
    #                                             and two_two not in mass_for_two and two_three not in mass_for_two:
    #                                         mass_group_products.append(
    #                                             [[mass_for_two[0], mass_for_two[1]], [two, two_two, two_three]])
    #                                         for two_four in unique_products:
    #                                             if two_four not in mass_for_two \
    #                                                     and two_two not in mass_for_two\
    #                                                     and two_three not in mass_for_two\
    #                                                     and two not in mass_for_two:
    #                                                 mass_group_products.append(
    #                                                     [[mass_for_two[0], mass_for_two[1]],
    #                                                      [two, two_two, two_three, two_four]])
    #
    #             else:
    #                 for two in range(len(unique_products), 0):
    #                     if unique_products[two] not in mass_for_two:
    #                         mass_group_products.append([mass_for_two, [two]])
    #                         for two_two in unique_products:
    #                             if two_two not in mass_for_two and two not in mass_for_two:
    #                                 mass_group_products.append([[mass_for_two[0], mass_for_two[1]], [two, two_two]])
    # if j <= n - 3:
    #     mass_for_three = []
    #     for i in mass_for_two:
    #         mass_for_three.append(i)
    #     mass_for_three.append(unique_products[len(mass_for_two) + 1])
    #
    #     for three in unique_products:
    #         if three not in mass_for_three:
    #             mass_group_products.append([mass_for_three, [three]])
    #             for three_two in unique_products:
    #                 if three_two not in mass_for_two:
    #                     mass_group_products.append([[mass_for_two[0], mass_for_two[1], mass_for_three[2]],
    #                     [three, three_two]])
    #
    #     for three in range(len(unique_products), 1):
    #         if unique_products[three] not in mass_for_two:
    #             mass_group_products.append([mass_for_three, [three]])
    #             for three_two in unique_products:
    #                 if three_two not in mass_for_two:
    #                     mass_group_products.append([[mass_for_two[0], mass_for_two[1], mass_for_three[2]], [three, three_two]])
    # else:
    #     mass_for_three = []
    #     for i in mass_for_two:
    #         mass_for_three.append(i)
    #     mass_for_three.append(unique_products[len(mass_for_two) + 1])
    #     for three in range(len(unique_products), 1):
    #         if unique_products[three] not in mass_for_two:
    #             mass_group_products.append([mass_for_three, [three]])
    #             for three_two in unique_products:
    #                 if three_two not in mass_for_two:
    #                     mass_group_products.append([[mass_for_two[0], mass_for_two[1], mass_for_three[2]], [three, three_two]])
    # if j <= n - 4:
    #     mass_for_four = [mass_for_three[0], mass_for_three[1], mass_for_three[2], unique_products[len(mass_for_three) + 1]]
    #     for four in unique_products:
    #         if four not in mass_for_four:
    #             mass_group_products.append([mass_for_four, [four]])
    #
    #     for four in range(len(unique_products), 1):
    #         if unique_products[four] not in mass_for_two:
    #             mass_group_products.append([[mass_for_four], [four]])
    # else:
    #     mass_for_four = [mass_for_three[0], mass_for_three[1], mass_for_three[2], unique_products[len(mass_for_three) + 1]]
    #     for four in range(len(unique_products), 1):
    #         if unique_products[four] not in mass_for_two:
    #             mass_group_products.append([[mass_for_four], [four]])

    mass_group_product = []
    n = len(unique_products)
    for count_items in range(2,  10):
        new = [0] * count_items
        for i in range(count_items - 1):
            start = 0
            for j in range(n):
                new[i] = start
                while new[i + 1] <= n and len(set(new)) == len(new) and \
                        list(set(add_x(new))) not in mass_group_product:
                # while new[i + 1] <= n:
                    mass_group_product.append(add_x(new))
                    new[i + 1] += 1
                else:
                    start += 1
                    new[i + 1] = 0

    # mass_group_product = find_repetitions(mass_group_product)
    # print_data(mass_group_products)
    print(len(mass_group_product))
    for i in mass_group_product:
        print(i)
