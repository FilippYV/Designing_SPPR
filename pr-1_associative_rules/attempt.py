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
    print(group_products_receipts)
    mass_group_products = [[['x'], ['x']]]
    count = 1
    last_len = 0
    for mass in group_products_receipts:
        start_time = time.time()
        print('-' * 25)
        print(f'Элемент {count} / {len(group_products_receipts)}')
        print('Количество элементов =', len(mass))
        if len(mass) > 4:
            n = 4
        else:
            n = len(mass)
        groups = []
        for count_item in range(1, n + 1):
            permutation = itertools.permutations(mass, count_item)
            comb_not_sort = []
            for comb in permutation:
                groups.append(list(comb))
        for i in range(len(groups)):
            for j in range(len(groups)):
                if i != j and set(groups[j]).isdisjoint(groups[i]) and set(groups[i]).isdisjoint(groups[j]):
                    on_off = True
                    for k in mass_group_products:
                        if sum(k, []) == sum([groups[j], groups[j]], []):
                            on_off = False
                    if on_off:
                        mass_group_products.append([groups[i], groups[j]])
        print("Время = %s seconds" % (time.time() - start_time))
        print(f"Получено сочетаний {len(mass_group_products) - last_len}")
        print(f'N = {n}')
        count += 1
        last_len = len(group_products_receipts)
    mass_group_products.pop(0)
    print('\n' * 2)
    print(len(mass_group_products))
