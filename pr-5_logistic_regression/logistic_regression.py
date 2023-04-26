import random
import math
import matplotlib.pyplot as plt


def generate_value(count):  # генерируем данные
    mass_data = []
    mass_answers = []
    for i in range(count):
        x = random.randint(100, 300)
        if x >= 240:
            mass_data.append(x / 1000)
            mass_answers.append(1)
        else:
            mass_data.append(x / 1000)
            mass_answers.append(0)
    print('\n' * 10)
    print(mass_data)
    print(mass_answers)
    return mass_data, mass_answers


def start_graph(mass_data, mass_answers, weights):
    mass_color = ['read', 'blue']
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for i in range(len(mass_data)):
        axis.scatter(mass_data[i], mass_answers[i], color=f'{mass_color[mass_answers[i]][0]}')
        # logist_model_answers = []
        # for i in range(len(mass_data)):
        sigmoid = 1 / (1 + math.e ** -(mass_data[i] * weights[0] + weights[1] * mass_answers[i]))
        # logist_model_answers.append(sigmoid)
        plt.scatter(mass_data[i], sigmoid, s=10, color='green')
    plt.title('Начальный граф распеределния')
    plt.xlabel('Количество баллов за 3 предмета')
    plt.ylabel('Распределение')
    plt.savefig('static//start_graph.png')
    # return logist_model_answers


def count_classifier_weight(data, answers, weights):
    for i in range(len(data)):
        logit = data[i] * weights[0] + answers[i] * weights[1]
        sigmoid = 1 / (1 + math.e ** -logit)
        if sigmoid >= 0.5 and answers[i] >= 0.5:
            new_weight = gradient_descent_one(sigmoid, data[i], answers[i])
        else:
            new_weight = gradient_descent_two(sigmoid, data[i], answers[i])
        for j in range(len(new_weight)):
            weights[j] = weights[j] - (new_weight[j])
    print(f'Результат: [{round(weights[0], 9)}, {round(weights[1], 9)}] | ', end='')
    return weights


def gradient_descent_one(sigmoid, data, answers):
    new_weight = [-data * (1 - sigmoid), -answers * (1 - sigmoid)]
    return new_weight


def gradient_descent_two(sigmoid, data, answers):
    new_weight = [-data * (0 - sigmoid), -answers * (0 - sigmoid)]
    return new_weight


def stop_graph(mass_data, mass_answers, weights):
    mass_color = ['read', 'blue']
    fig = plt.figure(figsize=(10, 7))
    axis = fig.add_subplot()
    for j in range(len(mass_data)):
        for i in range(len(mass_data) - 1):
            if mass_data[i] > mass_data[i + 1]:
                mass_data[i], mass_data[i + 1] = mass_data[i + 1], mass_data[i]
                mass_answers[i], mass_answers[i + 1] = mass_answers[i + 1], mass_answers[i]
    mass_answer_program = []
    for i in range(len(mass_data)):
        logit = mass_data[i] * weights[0] + mass_answers[i] * weights[1]
        sigmoid = 1 / (1 + math.e ** -logit)
        mass_answer_program.append(sigmoid)
    for i in range(len(mass_data)):
        axis.scatter(mass_data[i], mass_answers[i], color=f'{mass_color[mass_answers[i]][0]}')
        # axis.scatter(mass_data, mass_answer_program, s=10, color='green')
    plt.plot(mass_data, mass_answer_program, color='green')
    plt.title('Начальный граф распеределния')
    plt.xlabel('Количество баллов за 3 предмета')
    plt.ylabel('Распределение')
    plt.savefig('static//stop_graph.png')


def count_logloss(data, answers, classifier_weights):
    pass


if __name__ == '__main__':
    count_value = 100
    data, answers = generate_value(count_value)
    # classifier_weights = [random.random(), random.random()]
    classifier_weights = [0.653569605, 0.39508814945259281]
    print(f'Изначальные веса: {classifier_weights}')
    start_graph(data, answers, classifier_weights)
    for i in range(15):
        print(f'\nИтерация {i} |', end='')
        classifier_weights = count_classifier_weight(data, answers, classifier_weights)
        count_logloss(data, answers, classifier_weights)
    stop_graph(data, answers, classifier_weights)

    print('\nФинальная таблица')
    for i in range(len(data)):
        print(
            f'№{i} data = {data[i]}, aswer_y = {answers[i]}, {1 / (1 + math.e ** -(data[i] * classifier_weights[0] + answers[i] * classifier_weights[1]))}')
