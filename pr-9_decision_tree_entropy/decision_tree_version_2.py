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

def calculation_first_variable(count_data, unique_data, count_answer, unique_answer, massive_entropy):
    search_entropy = count_elements_calculate_entropy(unique_data, unique_answer)



if __name__ == '__main__':
    massive_tree = []
    massive_entropy = []

    x, y = generate_data()
    count_data, unique_data, count_answer, unique_answer = calculation_of_unique_values(x, y)
    massive_entropy.append(calculation_initial_entropy(count_answer, y))
    calculation_first_variable(count_data, unique_data, count_answer, unique_answer, massive_entropy)

