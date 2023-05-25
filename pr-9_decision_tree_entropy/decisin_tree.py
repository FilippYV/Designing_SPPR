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


if __name__ == '__main__':
    data, answers = generate_data()
    # Entropy = 1
    count_branches = []
    unique_elements = []
    for j in range(len(data[0])):
        mass_elements = []
        for i in range(len(data)):
            if data[i][j] not in mass_elements:
                mass_elements.append(data[i][j])
        unique_elements.append(mass_elements)
    unique_elements.append(list(set(answers)))
    print('unique_elements', unique_elements)
    count_elements = []
    for i in range(len(unique_elements) - 1):
        mass_elements = []
        for j in range(len(unique_elements[i])):
            count = 0
            for k in range(len(data)):
                if data[k][i] == unique_elements[i][j]:
                    count += 1
            mass_elements.append(count)
        count_elements.append(mass_elements)
    i = -1
    mass_elements = []
    for j in range(len(unique_elements[i])):
        count = 0
        for k in range(len(data)):
            if answers[k] == unique_elements[i][j]:
                count += 1
        mass_elements.append(count)
    count_elements.append(mass_elements)
    print('count_elements', count_elements)

    statr_entropy = - (count_elements[-1][0] / len(answers)) * math.log2(count_elements[-1][0] / len(answers)) - \
                    (count_elements[-1][1] / len(answers)) * math.log2(count_elements[-1][1] / len(answers))
    print('start_entropy = ', statr_entropy)

    # for h in range(len(unique_elements) - 1):
    #     division_elements = 0
    #     for g in range(len(unique_elements[h])):
    #         division_elements += unique_elements[h][g]
    #     division_elements /= len(unique_elements[h])
    search_entropy = []
    for i in range(len(unique_elements) - 1):
        mass_elements = []
        for j in range(len(unique_elements[i])):
            mass_answer_to_elem = [0] * len(data[0])
            for h in range(len(unique_elements[-1])):
                for k in range(len(data)):
                    if data[k][i] == unique_elements[i][j] and answers[k] == unique_elements[-1][h]:
                        mass_answer_to_elem[h] += 1
            mass_elements.append(mass_answer_to_elem)
        search_entropy.append(mass_elements)
    print('search_entropy', search_entropy)

    mass_entropy = []
    for i in range(len(search_entropy)):
        for j in range(len(search_entropy[i])):
            entropy = 0
            for k in range(len(search_entropy[i][j])):
                entropy += -(search_entropy[i][j][k] / count_elements[i][j]) * \
                           math.log2(search_entropy[i][j][k] / count_elements[i][j])
            mass_entropy.append(entropy)
    print('mass_entropy', mass_entropy)
    IG = [0] * len(data[0])
    print('IG', IG)
    for i in range(len(IG)):
        IG[i] += statr_entropy
        ig = 0
        for j in range(len(count_elements[i])):
            index = i * 2 + j
            ig += (count_elements[i][j] / len(data)) * mass_entropy[index]
        IG[i] -= ig
    print('IG', IG)
    max_ig = [-1, -1]
    for i in range(len(IG)):
        if IG[i] > max_ig[1]:
            max_ig = [i, IG[i]]
    print(f'Выбираем {max_ig[0]}ую переменнную в качестве первего узла')
    print(
        f'  Еcли x{max_ig[0]} элемент = 1 то ответ в {search_entropy[max_ig[0]][0][1]} случаях правильынй, {search_entropy[max_ig[0]][1][1]} случаях не правильынй,')
    print(
        f'  Энтропия = {mass_entropy[0]}')
    print(f'    Выбираем {1}ую переменнную в качестве второго узла')
    print(f'    Энтропия = 0')
    print(
        f'  Еcли x{max_ig[0]} элемент = 0 то ответ в {search_entropy[max_ig[0]][0][0]} случаях правильынй, {search_entropy[max_ig[0]][1][0]} случаях не правильынй,')
    print(
        f'  Энтропия = {mass_entropy[1]}')
    print(f'    Выбираем {1}ую переменнную в качестве второго узла')
    print(f'    Энтропия = 0')
    # print('\n' * 5)
    mass_element_to_tree = []
    mass_element_to_tree.append(max_ig[0])
    #
    print('new_unique_elements', unique_elements)
    print('new_count_elements', count_elements)
    # search_entropy_for_two = [0, 0]
    # new_entropy = []
    # for h in range(len(unique_elements) - 1):
    #     for u in range(len(unique_elements[-1])):
    #         mass_1 = []
    #         for y in range(len(unique_elements[h])):
    #             mass_2 = []
    #             for t in range(len(unique_elements[-1])):
    #                 count = 0
    #                 for i in range(len(data)):
    #                     if data[i][mass_element_to_tree[-1]] == unique_elements[mass_element_to_tree[-1]][u] \
    #                             and data[i][h] == unique_elements[y] and answers[i] == unique_elements[-1]:
    #                             count += 1
    #                 mass_2.append(count)
    #             mass_1.append(mass_2)
    #         new_entropy.append(mass_1)
    # print(new_entropy, 'new_entropy')
    # exit()
    entropy_two = [0] * len(unique_elements[0]) * len(unique_elements[1]) * len(unique_elements[2])

    for i in range(len(data)):
        if data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 1 and answers[i] == 0:
            entropy_two[0] += 1
        elif data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 1 and answers[i] == 1:
            entropy_two[1] += 1
        elif data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 0 and answers[i] == 0:
            entropy_two[2] += 1
        elif data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 0 and answers[i] == 1:
            entropy_two[3] += 1
        elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 0 and answers[i] == 0:
            entropy_two[4] += 1
        elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 0 and answers[i] == 1:
            entropy_two[5] += 1
        elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 1 and answers[i] == 0:
            entropy_two[6] += 1
        elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 1 and answers[i] == 1:
            entropy_two[7] += 1
    # for i in range(len(data)):
    #     if data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 1 and answers[i] == 0:
    #         entropy_two[0] += 1
    #     elif data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 1 and answers[i] == 1:
    #         entropy_two[1] += 1
    #     elif data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 0 and answers[i] == 0:
    #         entropy_two[2] += 1
    #     elif data[i][mass_element_to_tree[-1]] == 0 and data[i][1] == 0 and answers[i] == 1:
    #         entropy_two[3] += 1
    #     elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 0 and answers[i] == 0:
    #         entropy_two[4] += 1
    #     elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 0 and answers[i] == 1:
    #         entropy_two[5] += 1
    #     elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 1 and answers[i] == 0:
    #         entropy_two[6] += 1
    #     elif data[i][mass_element_to_tree[-1]] == 1 and data[i][1] == 1 and answers[i] == 1:
    #         entropy_two[7] += 1
    print("\nentropy_two", entropy_two)
    # for i in range(len(entropy_two)):
    #
    mass_entropy = []
    # for i in range(len(search_entropy)):
    #     for j in range(len(search_entropy[i])):
    #         entropy = 0
    #         for k in range(len(search_entropy[i][j])):
    #             entropy += -(search_entropy[i][j][k] / count_elements[i][j]) * \
    #                        math.log2(search_entropy[i][j][k] / count_elements[i][j])
    #         mass_entropy.append(entropy)
    # print('mass_entropy', mass_entropy)
    # IG = [0] * len(data[0])
    # print('IG', IG)
    # for i in range(len(IG)):
    #     IG[i] += statr_entropy
    #     ig = 0
    #     for j in range(len(count_elements[i])):
    #         index = i * 2 + j
    #         ig += (count_elements[i][j] / len(data)) * mass_entropy[index]
    #     IG[i] -= ig
    # print('IG', IG)
    # max_ig = [-1, -1]
    # for i in range(len(IG)):
    #     if IG[i] > max_ig[1]:
    #         max_ig = [i, IG[i]]
    #

    # print('tree')
    # print(
    #     f'  Ели x{max_ig[0]} элемент = 1 то ответ в {search_entropy[max_ig[0]][0][1]} случаях правильынй, {search_entropy[max_ig[0]][1][1]} случаях не правильынй,')
    # print(f'     ДАЛЕЕ ПРИ x{1} элемент = 1 то ответ в {entropy_two[3]} случаях правильынй, {entropy_two[2]} случаях не правильынй,')
    # print(
    #     f'  Ели x{max_ig[0]} элемент = 0 то ответ в {search_entropy[max_ig[0]][0][0]} случаях правильынй, {search_entropy[max_ig[0]][1][0]} случаях не правильынй,')
    # print(
    #     f'     ДАЛЕЕ ПРИ x{1} элемент = 1 то ответ в {entropy_two[4]} случаях правильынй, {entropy_two[3]} случаях не правильынй,')
    # print('tree')
    # print('x0 = 1')
    # print('     x1 = 0')
    # print('x1 = 0')
    # print('     x1 = 1')

    #
    #         mass_elements.append(count)
    #     count_elements.append(mass_elements)
    # i = -1
