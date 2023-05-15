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


def calculation_of_unique_values(x):
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
    print()
    return unique_data, count_data


def calculation_of_unique_responses(y):
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
    print()
    return unique_answer, count_answer


def count_start_entropy(count_answer):
    # рачсёт начальной энтропии
    start_entropy = 0
    for i in count_answer:
        start_entropy -= (i / len(y)) * math.log2(i / len(y))
    print('Начальная энтропия =', start_entropy)
    print()
    return start_entropy


def count_entropy_outcomes():
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
    print()
    return search_entropy


def count_ig(search_entropy):
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
        IG[i] -= ig
    print('IG', IG)
    print()
    return  IG

def selection_criteria(IG):
    # выбор первого критерия
    max = 0
    iteration = 0
    for i in range(len(IG)):
        if max < IG[i]:
            max = IG[i]
            iteration = i
    print('IG =', max, '\nКритерий =', iteration)
    print()
    tree.append(iteration)
    print('Полученное дерево')
    for i in tree:
        print(i)
    print()


if __name__ == '__main__':
    tree = []
    x, y = generate_data()
    unique_data, count_data = calculation_of_unique_values(x)
    unique_answer, count_answer = calculation_of_unique_responses(y)
    start_entropy = count_start_entropy(count_answer)
    search_entropy = count_entropy_outcomes()
    ig = count_ig(search_entropy)
    selection_criteria(ig)