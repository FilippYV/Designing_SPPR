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
    return data, answers


def calculation_of_unique_values(x, y):
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
    print()
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
    print()
    # все уникальные ответы и их количества
    unique_answer = []
    for i in y:
        if i not in unique_answer:
            unique_answer.append(i)
    unique_answer.sort()
    print('Уникальные классы:', unique_answer)
    print()
    count_answer = []
    for i in unique_answer:
        count = 0
        for j in y:
            if j == i:
                count += 1
        count_answer.append(count)
    print('Количество для уникальных классов:', count_answer)
    print()
    return count_data, unique_data, count_answer, unique_answer


def calculation_initial_entropy(count_answer, y):
    # рачсёт начальной энтропии
    start_entropy = 0
    for i in count_answer:
        start_entropy -= (i / len(y)) * math.log2(i / len(y))
    print('Начальная энтропия =', start_entropy)
    print()
    return start_entropy


def count_elements_calculate_entropy(unique_data, unique_answer):
    # Kоличество элементов для подсчёта энтропии
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
    print()
    return search_entropy


def entropy_calculation_for_all_initial_outcomes(search_entropy, massive_entropy, massive_tree):
    # расчёт энтропии для всех начальных исходов
    mass_entropy = []
    for i in range(len(search_entropy)):
        entropy_critery = []
        for j in range(len(search_entropy[i])):
            entropy = 0
            for k in range(len(search_entropy[i][j])):
                if search_entropy[i][j][k] / count_data[i][j] > 0:
                    entropy += -(search_entropy[i][j][k] / count_data[i][j]) * \
                               math.log2(search_entropy[i][j][k] / count_data[i][j])
                else:
                    entropy += 0
            entropy_critery.append(entropy)
        mass_entropy.append(entropy_critery)
    print('mass_entropy', mass_entropy)
    IG = [0] * len(unique_data)
    # print('IG', IG)
    for i in range(len(IG)):
        IG[i] += massive_entropy[-1]
        ig = 0
        for j in range(len(count_data[i])):
            ig += (count_data[i][j] / (len(x))) * mass_entropy[i][j]
        IG[i] -= ig
    print('IG', IG)
    maximum = [0, 0]
    for i, ii in enumerate(IG):
        if ii > maximum[1]:
            maximum = [i, ii]
    print(maximum)
    print()
    massive_tree.append([maximum[0]])
    massive_entropy.append(mass_entropy[maximum[0]])


def calculation_first_variable(count_data, unique_data, count_answer, unique_answer, massive_entropy, massive_tree):
    search_entropy = count_elements_calculate_entropy(unique_data, unique_answer)
    entropy_calculation_for_all_initial_outcomes(search_entropy, massive_entropy, massive_tree)


def calculation_new_entropy(new_entropy):
    summ_ent = []
    for i in new_entropy:
        mass = []
        for j in i:
            count = 0
            for k in j:
                count += k
            mass.append(count)
        summ_ent.append(mass)
    print(summ_ent)
    return summ_ent


def calculate_next_entropy(massive_tree, massive_entropy, count_data, unique_data, count_answer, unique_answer, x, y):
    new_entropy = []
    for i in unique_answer:
        mass_1 = []
        for j in unique_data[0]:
            mass_2 = []
            for k in unique_data[1]:
                count = 0
                for d, dd in enumerate(x):
                    if x[d][0] == j and x[d][1] == k and y[d] == i:
                        count += 1
                mass_2.append(count)
            mass_1.append(mass_2)
        new_entropy.append(mass_1)
    print(new_entropy)
    summ_ent = calculation_new_entropy(new_entropy)
    mass_entropy = []
    for i, ii in enumerate(new_entropy):
        # расчёт энтропии для всех начальных исходов
        entropy_critery = []
        for j in range(len(ii)):
            entropy = 0
            for k in range(len(ii[j])):
                if ii[j][k] / summ_ent[i][j] > 0:
                    entropy += -(ii[j][k] / summ_ent[i][j]) * \
                               math.log2(ii[j][k] / summ_ent[i][j])
                else:
                    entropy += 0
            entropy_critery.append(entropy)
        mass_entropy.append(entropy_critery)
    print('mass_entropy', mass_entropy)
    IG = [0] * len(unique_data)
    # print('IG', IG)
    for i in range(len(IG)):
        IG[i] += massive_entropy[-1][0]
        ig = 0
        for j in range(len(count_data[i])):
            ig += (count_data[i][j] / (len(x))) * mass_entropy[i][j]
        IG[i] -= ig
    print('IG', IG)
    massive_entropy.append(mass_entropy)
    massive_tree.append([1, 1])
    print()
    return new_entropy


if __name__ == '__main__':
    massive_tree = []
    massive_entropy = []

    x, y = generate_data()
    count_data, unique_data, count_answer, unique_answer = calculation_of_unique_values(x, y)
    massive_entropy.append(calculation_initial_entropy(count_answer, y, ))
    calculation_first_variable(count_data, unique_data, count_answer, unique_answer, massive_entropy, massive_tree)
    calculate_next_entropy(massive_tree, massive_entropy, count_data, unique_data, count_answer, unique_answer, x, y)
    print()
    print(f'Дерво:')
    for i in massive_tree:
        print(i)
    print()
    print(f'Ентропия на всех участках дерева:')
    for i in massive_entropy:
        print(i)
