import math
data_nature = [
        [10, 50, "гусеница"],
        [20, 30, "божья коровка"],
        [25, 30, "божья коровка"],
        [20, 60, "гусеница"],
        [15, 70, "гусеница"],
        [40, 40, "божья коровка"],
        [30, 45, "божья коровка"],
        [20, 45, "гусеница"],
        [40, 30, "божья коровка"],
        [7, 35, "гусеница"]]

answers = []
for indx, mass in enumerate(data_nature):
    if data_nature[indx][-1] == "гусеница":
        answers.append(1)
    else:
        answers.append(0)
unique_answers = list(set(answers))
unique_answers = [1,0]
print(answers, unique_answers)
expectation = [] #матожидание
variance = [] #дисперсия
for l in range(len(data_nature[0])-1):
    datas_mass = []
    for x in range(len(list(set(answers)))):
        count = 0
        count_value = 0
        for i in range(len(data_nature)):
            if answers[i] == unique_answers[x]:
                count_value += data_nature[i][l]
                count += 1
        print(f'expectation for criterion {l}, for value {x} = 1/{count} * ({count_value}) = {(1/count) * count_value}')
        datas_mass.append((1/count) * count_value)
    expectation.append(datas_mass)
print('expectation =',expectation)
for l in range(len(data_nature[0])-1):
    datas_mass = []
    for x in range(len(list(set(answers)))):
        count = 0
        count_value = 0
        for i in range(len(data_nature)):
            if answers[i] == unique_answers[x]:
                count_value += (data_nature[i][l] - expectation[l][x]) ** 2
                count += 1
        print(f'variance for criterion {l}, for value {x} = (1/({count}-1)) * ({count_value}) = {(1/(count-1)) * count_value}')
        datas_mass.append((1/(count-1)) * count_value)
    variance.append(datas_mass)
print()
print('expectation =',expectation)
print('variance =',variance)

ver = []
for i in range(len(unique_answers)):
    count = 0
    for j in range(len(answers)):
        if unique_answers[i] == answers[j]:
            count += 1
    ver.append(count/len(answers))
print(ver)
input_data = [10, 50] # задаём данные
final_value = []
for i in range(len(unique_answers)):
    value = ver[i] *  (1 / (math.sqrt(2*math.pi* variance[i][0] * variance[i][1]))) *\
    (((input_data[0] - expectation[i][0])**2)/(2 * variance[i][0] ** 2) - ((input_data[1] - expectation[i][1])**2)/(2 * variance[i][1] ** 2))
    final_value.append(value)
print(final_value)
maximum = [None, -111111]
for i, mass in enumerate(final_value):
    if mass > maximum[-1]:
        maximum = [i, mass]
if maximum[0] == 0:
    print('0 - гусеница')
else:
    print('1 - божья коровка')