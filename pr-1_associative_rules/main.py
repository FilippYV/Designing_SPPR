import pandas as pd
import itertools
import time

data = pd.read_csv('static/data//new_data.csv')
unique_receipts = data.receipt_number.unique()
print(len(unique_receipts))
print(unique_receipts)

count_receipt = len(unique_receipts)
unique_products = data['product'].unique()
print(len(unique_products))
print(unique_products)

data_np = data.to_numpy()

group_products_receipts = []
for i in unique_receipts:
    micro_data = []
    for j in data_np:
        if j[0] == i:
            micro_data.append(j[1])
    group_products_receipts.append(micro_data)


mass_group_products = []
mass_group_products_str = []
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
    print(f'Максимум элементов = {n}')
    groups = []
    for count_item in range(1, n + 1):
        permutation = itertools.permutations(mass, count_item)
        comb_not_sort = []
        for comb in permutation:
            groups.append(list(comb))
    for i in range(len(groups)):
        for j in range(len(groups)):
            if i != j and set(groups[j]).isdisjoint(groups[i]) and set(groups[i]).isdisjoint(groups[j]):
                if sum([groups[i], groups[j]], []) not in mass_group_products_str:
                    mass_group_products_str.append(sum([groups[i], groups[j]], []))
                    mass_group_products.append([groups[i], groups[j]])
    print("Время = %s seconds" % (time.time() - start_time))
    print(f"Получено сочетаний {len(mass_group_products) - last_len}")
    print(f"Всего элементов = {len(mass_group_products)}")
    count += 1
    last_len = len(group_products_receipts)
print('\n' * 1)
print(len(mass_group_products))

for i in range(len(mass_group_products)):
    count = 0
    for j in group_products_receipts:
        if set(mass_group_products[i][0]).issubset(j) and set(mass_group_products[i][1]).issubset(j):
            count += 1
    if i == 0:
        print(f'{count*100}/{count_receipt} = {round((count*100/count_receipt),2)}')
    mass_group_products[i].append((round((count*100/count_receipt),2)))


for i in range(len(mass_group_products)):
    count_one = 0
    count_two = 0
    for j in group_products_receipts:
        if set(mass_group_products[i][0]).issubset(j) and set(mass_group_products[i][1]).issubset(j):
            count_one += 1
    for j in group_products_receipts:
        if set(mass_group_products[i][0]).issubset(j):
            count_two += 1
    if count_two != 0:
        mass_group_products[i].append((round((count_one*100/count_two),2)))
    else:
        mass_group_products[i].append(0)

for i in range(len(mass_group_products)):
    count_one = 0
    for j in group_products_receipts:
        if set(mass_group_products[i][1]).issubset(j):
            count_one += 1
    if (count_one*100/count_receipt) != 0:
        mass_group_products[i].append((round(mass_group_products[i][-1]/(count_one*100/count_receipt),2)))
    else:
        mass_group_products[i].append(0)

name_for_index = []
for i in range(len(mass_group_products)):
    name_A = ''
    name_B = ''
    for k in range(len(mass_group_products[i][0])):
        len_name = len(mass_group_products[i][0])
        if k != len_name - 1 and len_name != 1:
            name_A += f'{mass_group_products[i][0][k]}, '
        else:
            name_A += f'{mass_group_products[i][0][k]}'
    for k in range(len(mass_group_products[i][1])):
        len_name = len(mass_group_products[i][1])
        if k != len_name - 1 and len_name != 1:
            name_B += f'{mass_group_products[i][1][k]}, '
        else:
            name_B += f'{mass_group_products[i][1][k]}'
    string = f'{name_A} | {name_B}'
    name_for_index.append(string)

dataframe = []
for i in range(len(mass_group_products)):
    mass = []
    for j in range(len(mass_group_products[i])):
        if j != 0 and j != 1:
            mass.append(mass_group_products[i][j])
    dataframe.append(mass)

Dataframe = pd.DataFrame(dataframe, columns =['Suported', 'Reliability', 'Lift'], index=name_for_index)
Dataframe = (Dataframe.loc[Dataframe.Suported < 89])
Dataframe = (Dataframe.loc[20 < Dataframe.Suported])
Dataframe = (Dataframe.loc[30 < Dataframe.Reliability])
Dataframe = (Dataframe.loc[Dataframe.Reliability < 70])

print(Dataframe.sort_values('Lift', ascending=False).head(40))