import itertools
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
    print(group_products_receipts)
    mass_group_products = []
    count = 0
    for mass in group_products_receipts:
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
        print(f'N = {n}')
        print('Количество элементов =', len(mass))
        for i in range(len(groups)):
            for j in range(len(groups)):
                if i != j and set(groups[j]).isdisjoint(groups[i]) and set(groups[i]).isdisjoint(groups[j]) and \
                        [groups[i], groups[j]] not in mass_group_products:
                    mass_group_products.append([groups[i], groups[j]])
        print('-'*25)
        print(f'Элемент {count} / {len(group_products_receipts)}')
        count += 1
    print('\n' * 10)
    print(len(mass_group_products))
    print(mass_group_products)

    # for i in group_products:
    #     print(i)
