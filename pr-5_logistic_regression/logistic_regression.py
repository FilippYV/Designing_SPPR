import random
import math
import matplotlib.pyplot as plt


def generate_value(count):  # генерируем данные
    mass_data = []
    mass_answers = []
    mass_data = [[0.46, 0.43],
                 [0.62, 0.36],
                 [0.53, 0.93],
                 [0.73, 0.12],
                 [0.5, 0.91],
                 [0.82, 0.08],
                 [0.03, 1.0],
                 [0.82, 0.21],
                 [0.4, 0.18],
                 [0.25, 0.01]]
    mass_answers = [0, 0, 1, 0, 1, 0, 1, 1, 0, 0]

    # for i in range(count):
    #     x = random.randint(0, 100)
    #     y = random.randint(0, 100)
    #     if x + y >= 100:
    #         mass_data.append([x / 100, y / 100])
    #         mass_answers.append(1)
    #     else:
    #         mass_data.append([x / 100, y / 100])
    #         mass_answers.append(0)

    # for i in mass_data:
    #     print(str(i[1]).replace('.', ','))
    #     # x = x.replace('.', ',')
    #     # print(x)
    # print("mass_answers")
    # for i in mass_answers:
    #     print(i)
    print(mass_data)
    print(mass_answers)
    return mass_data, mass_answers


def start_graph(mass_data, mass_answers, weights):
    mass_color = ['read', 'blue']
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for i in range(len(mass_data)):
        axis.scatter(mass_data[i][0], mass_data[i][1], color=f'{mass_color[mass_answers[i]][0]}')
        sigmoid = 1 / (1 + math.e ** -(mass_data[i][0] * weights[0] + weights[1] * mass_data[i][1]))
        plt.scatter(mass_data[i][0], sigmoid, s=10, color='green')
    plt.title('Начальный граф распеределния')
    plt.xlabel('Количество баллов за 3 предмета')
    plt.ylabel('Распределение')
    plt.savefig('static//start_graph.png')
    # return logist_model_answers


def calculation_program_answer(data, answers, classifier_weights):
    program_answer = []
    # loggit_table = []
    # sigmoid_table = []
    for i in range(len(data)):
        logit = classifier_weights[0] + data[i][0] * classifier_weights[1] + data[i][1] * classifier_weights[2]
        # print(f'{logit} = {classifier_weights[0]} + {data[i][0]} * {classifier_weights[1]} + {data[i][1]} *'
        #       f' {classifier_weights[2]}')
        # loggit_table.append(logit)
        sigmoid = 1 / (1 + math.e ** (-logit))
        # sigmoid_table.append(sigmoid)
        # print(f"{sigmoid} = 1 / (1 + math.e ** {(-logit)})")
        # print()
        program_answer.append(sigmoid)
    # exit(123)
    # for i in sigmoid_table:
    #     print(round(i,2))

    return program_answer


def count_logloss(data, answers, classifier_weights, program_answer):
    logloss = 0
    for i in range(len(data)):
        logloss += math.log(program_answer[i]) * answers[i] + (1 - answers[i]) * math.log(1 - program_answer[i] + 1e-30)
        # x = f"{round(answers[i], 2)} * log({round(program_answer[i], 2)}) + (1 - {round(answers[i], 2)}) + log(1 - {round(program_answer[i], 2)})"
        # print(f"({x.replace('.', ',')})")
    logloss = (-logloss) / len(data)
    print(f'logloss = {logloss}')
    # exit()
    return logloss


def count_classifier_weight(data, answers, classifier_weights):
    for i in range(len(data)):
        logit = classifier_weights[0] + data[i][0] * classifier_weights[1] + data[i][1] * classifier_weights[2]
        sigmoid = 1 / (1 + math.e ** (-logit))
        classifier_weights[0] -= -(answers[i] - sigmoid)
        classifier_weights[1] -= -(answers[i] - sigmoid) * data[i][0]
        classifier_weights[2] -= -(answers[i] - sigmoid) * data[i][1]
        # print(f"{round(classifier_weights[0], 2)} -= -({round(answers[i], 2)} - {round(sigmoid, 2)})")
        # print(
        #     f"{round(classifier_weights[1], 2)} -= -({round(answers[i], 2)} - {round(sigmoid, 2)}) * {round(data[i][0], 2)}")
        # print(
        #     f"{round(classifier_weights[2], 2)} -= -({round(answers[i], 2)} - {round(sigmoid, 2)}) * {round(data[i][1], 2)}")

        # exit(123)
    print(f'Результат: [{round(classifier_weights[0], 9)}, {round(classifier_weights[1], 9)},'
          f' {round(classifier_weights[2], 9)}] | ', end='')
    print()
    return classifier_weights


def graph_logloss(logloss):
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    iteration = []
    for i in range(len(logloss)):
        iteration.append(i)
    for i, data in enumerate(logloss):
        axis.scatter(i, data, s=50, color='red')
    plt.plot(iteration, logloss)
    plt.title('График изменения logloss')
    plt.xlabel('Итерации')
    plt.ylabel('logloss')
    plt.savefig('static//graph_logloss.png')


def stop_graph(mass_data, mass_answers, weights, program_answer):
    mass_color = ['read', 'green']
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    summ_point_exam = []
    for i in data:
        summ_point_exam.append(i[0] + i[1])
    for j in range(len(summ_point_exam)):
        for i in range(len(summ_point_exam) - 1):
            if summ_point_exam[i] > summ_point_exam[i + 1]:
                summ_point_exam[i], summ_point_exam[i + 1] = summ_point_exam[i + 1], summ_point_exam[i]
                mass_data[i], mass_data[i + 1] = mass_data[i + 1], mass_data[i]
                mass_answers[i], mass_answers[i + 1] = mass_answers[i + 1], mass_answers[i]
                program_answer[i], program_answer[i + 1] = program_answer[i + 1], program_answer[i]
    mass_sigm = []
    for i in range(len(mass_data)):
        logit = classifier_weights[0] + data[i][0] * classifier_weights[1] + data[i][1] * classifier_weights[2]
        sigmoid = 1 / (1 + math.e ** (-logit))
        mass_sigm.append(sigmoid)
        axis.scatter(summ_point_exam[i], sigmoid, color=f'{mass_color[mass_answers[i]][0]}')
    plt.plot(summ_point_exam, mass_sigm, color='orange')
    plt.axhline(y=0.5, color='black', linestyle='-')
    plt.title('Конечный граф распеределния')
    plt.savefig('static//stop_graph.png')


def predict(x, y):
    print(f'predict: x = {(x + y) * 100}')
    print(f'1-ый элемент - {x}')
    print(f'2-ой элемент - {y}')
    print('Вероятность отсенения к 1 классу', end=' = ')
    print(
        f'{1 / (1 + math.e ** -(classifier_weights[0] + x * classifier_weights[1] + y * classifier_weights[2]))}')
    print('Вероятность отсенения к 0 классу', end=' = ')
    print(
        f'{1 - (1 / (1 + math.e ** -(classifier_weights[0] + x * classifier_weights[1] + y * classifier_weights[2])))}')
    print()


if __name__ == '__main__':
    count_value = 10
    logloss = []
    data, answers = generate_value(count_value)
    # classifier_weights = [random.random(), random.random(), random.random()]
    classifier_weights = [0.653569605, 0.39508814945259281, 1.153569605]
    print(f'Изначальные веса: {classifier_weights}')
    start_graph(data, answers, classifier_weights)
    program_answer = calculation_program_answer(data, answers, classifier_weights)
    count_interation = 50
    for iteration in range(count_interation):
        print(f'\nИтерация {iteration} |', end='')
        program_answer = calculation_program_answer(data, answers, classifier_weights)
        logloss.append(count_logloss(data, answers, classifier_weights, program_answer))
        classifier_weights = count_classifier_weight(data, answers, classifier_weights)

    stop_graph(data, answers, classifier_weights, program_answer)
    graph_logloss(logloss)

    print('\nФинальная таблица')
    for i in range(len(data)):
        print(
            f'№{i} data = {data[i]}| y = {answers[i]}| y_p = {program_answer[i]}')
    print()

    predict(0.75, 0.25)
    predict(0.99, 0.99)
    predict(0.25, 0.25)
