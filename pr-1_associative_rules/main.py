import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib as plt

data = pd.read_csv('C:/Users/filip/PycharmProjects/Firs_task_Zeleznyak/static//data.csv')
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
dataframe = pd.DataFrame({'receipt': unique_receipts,

                          'product': group_products_receipts},
                         columns=['receipt', 'product'])
procent_product_in_receipt = []
len_dataframe = len(dataframe)
count_product_procent_ = []
for x in unique_products:
    count_product = 0
    for i in group_products_receipts:
        switch = False
        for j in i:
            if j == x:
                switch = True
        if switch:
            count_product += 1
    count_product_procent_.append(count_product)
for i in range(len(count_product_procent_)):
    count_product_procent_[i] = round(count_product_procent_[i]/len_dataframe, 2)
count_product_procent = []
for i in range(len(count_product_procent_)):
    if count_product_procent_[i] >= 0.2:
        count_product_procent.append([unique_products[i], count_product_procent_[i]])
mass_two_product = []
for i in range(len(count_product_procent)-1):
    for j in range(i + 1, len(count_product_procent)):
        mass_two_product.append([count_product_procent[i][0], count_product_procent[j][0]])
suported_mass_two_product_ = []
for x in mass_two_product:
    count = 0
    for i in group_products_receipts:
        if x[0] in i and x[1] in i:
            count += 1
    suported_mass_two_product_.append(count)
for i in range(len(suported_mass_two_product_)):
    suported_mass_two_product_[i] = round(suported_mass_two_product_[i] * 100 / len_dataframe, 2)
suported_mass_two_product = []
for i in range(len(mass_two_product)):
    suported_mass_two_product.append([mass_two_product[i][0], mass_two_product[i][1], suported_mass_two_product_[i]])
for i in range(len(suported_mass_two_product)):
    print(f'{suported_mass_two_product[i][0]}, {suported_mass_two_product[i][1]} = {suported_mass_two_product[i][2]}%')
reliability_mass_two_product_ = []
reliability_mass_two_product__ = []
for x in mass_two_product:
    count = 0
    for i in group_products_receipts:
        if x[0] in i and x[1] in i:
            count += 1
    reliability_mass_two_product_.append(count)
for x in mass_two_product:
    count_firs = 0
    for i in group_products_receipts:
        if x[0] in i:
            count_firs += 1
    reliability_mass_two_product__.append(count_firs)
for i in range(len(suported_mass_two_product)):
    reliability_mass_two_product_[i] = round(reliability_mass_two_product_[i] * 100 / reliability_mass_two_product__[i], 2)
reliability_mass_two_product = []
for i in range(len(mass_two_product)):
    reliability_mass_two_product.append([mass_two_product[i][0], mass_two_product[i][1], reliability_mass_two_product_[i]])
for i in range(len(reliability_mass_two_product)):
    print(f'{reliability_mass_two_product[i][0]}, {reliability_mass_two_product[i][1]} = {reliability_mass_two_product[i][2]}%')
lift_mass_two_product_ = []
lift_mass_two_product__ = []

for i in range(len(reliability_mass_two_product)):
    lift_mass_two_product_.append(reliability_mass_two_product[i][2])

for x in mass_two_product:
    count_second = 0
    for i in group_products_receipts:
        if x[1] in i:
            count_second += 1
    lift_mass_two_product__.append(count_second)

for i in range(len(lift_mass_two_product_)):
    lift_mass_two_product__[i] = round(lift_mass_two_product__[i] * 100 / len_dataframe)


lift_mass_two_product = []
for i in range(len(mass_two_product)):
    lift_mass_two_product.append([mass_two_product[i][0], mass_two_product[i][1], round(lift_mass_two_product_[i]/lift_mass_two_product__[i], 2)])


for i in range(len(lift_mass_two_product)):
    print(f'{lift_mass_two_product[i][0]}, {lift_mass_two_product[i][1]} = {lift_mass_two_product[i][2]}%')