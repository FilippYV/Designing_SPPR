import math


def generate_data():
    data = [[1, 0],
            [1, 0],
            [1, 0],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1]]
    answers = [1, 1, 1, 1, 0, 0, 0, 0]
    for i in answers:
        print(i)
    return data, answers


x, y = generate_data()
mass_entropy_ = []
# все уникальне критерии и их количества
unique_data = []
for j in range(len(x[0])):
    mass_to_unique = []
    for i in range(len(x)):
        if x[i][j] not in mass_to_unique:
            mass_to_unique.append(x[i][j])
    mass_to_unique.sort()
    unique_data.append(mass_to_unique)
print('Уникальные значения у критериев:', unique_data)

count_data = []
for i in range(len(unique_data)):
    mass_to_unique = []
    for j in range(len(unique_data[i])):
        count = 0
        for k in range(len(x)):
            if x[k][i] == unique_data[i][j]:
                count += 1
        mass_to_unique.append(count)
    count_data.append(mass_to_unique)
print('Количество значений у критериев:', count_data)
# все уникальные ответы и их количества
unique_answer = []
for i in y:
    if i not in unique_answer:
        unique_answer.append(i)
unique_answer.sort()
print('Уникальные классы:', unique_answer)

count_answer = []
for i in unique_answer:
    count = 0
    for j in y:
        if j == i:
            count += 1
    count_answer.append(count)
print('Количество для уникальных классов:', count_answer)
# рачсёт начальной энтропии
start_entropy = 0
for i in count_answer:
    start_entropy -= (i / len(y)) * math.log2(i / len(y))
print('Начальная энтропия =', start_entropy)
mass_entropy_.append(start_entropy)
# расчёт энтропии для всех исходов
search_entropy = []
for criterion in range(len(unique_data)):
    count_criterion = []
    for unique_criterion in range(len(unique_data[criterion])):
        mass_answer_to_elem = [0] * len(unique_data)
        for h in range(len(unique_answer)):
            for i in range(len(x)):
                if x[i][criterion] == unique_data[criterion][unique_criterion] and y[i] == unique_answer[h]:
                    mass_answer_to_elem[h] += 1
        count_criterion.append(mass_answer_to_elem)
    search_entropy.append(count_criterion)
print('Kоличество элементов для подсчёта энтропии:', search_entropy)

# расчёт энтропии для всех начальных исходов
mass_entropy = []
for i in range(len(search_entropy)):
    entropy_critery = []
    for j in range(len(search_entropy[i])):
        entropy = 0
        for k in range(len(search_entropy[i][j])):
            entropy += -(search_entropy[i][j][k] / count_data[i][j]) * \
                       math.log2(search_entropy[i][j][k] / count_data[i][j])
        entropy_critery.append(entropy)
    mass_entropy.append(entropy_critery)
print('mass_entropy', mass_entropy)
IG = [0] * len(unique_data)
# print('IG', IG)
for i in range(len(IG)):
    IG[i] += start_entropy
    ig = 0
    for j in range(len(count_data[i])):
        ig += (count_data[i][j] / (len(x))) * mass_entropy[i][j]
        # print(count_data[i][j])
    IG[i] -= ig
print('IG', IG)

# выбор первого критерия
tree = []
max = 0
iteration = 0
for i in range(len(IG)):
    if max < IG[i]:
        max = IG[i]
        iteration = i
        mass_entropy_.append(mass_entropy[i])

print('IG =', max, '\nКритерий =', iteration)
tree.append(iteration)
print(tree)

countss  = []
for i in unique_data[tree[0]]:
    count2 = []
    for j in unique_data[1]:
        count1 = []
        for yy in unique_answer:
            count = 0
            for h, hh in enumerate(x):
                if hh[0] == i and hh[1] == j and y[h] == 0:
                    count += 1
            count1.append(count)
        count2.append(count1)
    countss.append(count2)
print(countss)

search_entropy = countss
mass_entropy = []
start_entropy = mass_entropy
for i in range(len(search_entropy)):
    entropy_critery = []
    for j in range(len(search_entropy[i])):
        entropy = 0
        for k in range(len(search_entropy[i][j])):
            if count_data[i][j] > 0 :
                entropy += -(search_entropy[i][j][k] / count_data[i][j]) * math.log2(search_entropy[i][j][k] / count_data[i][j])
            else:
                entropy += 0
        entropy_critery.append(entropy)
    mass_entropy.append(entropy_critery)
print('mass_entropy', mass_entropy)
IG = [0] * len(unique_data)
# print('IG', IG)
for i in range(len(IG)):
    IG[i] += start_entropy
    ig = 0
    for j in range(len(count_data[i])):
            ig += (count_data[i][j] / (len(x))) * mass_entropy[i][j]
            # print(count_data[i][j])
    IG[i] -= ig
print('IG', IG)