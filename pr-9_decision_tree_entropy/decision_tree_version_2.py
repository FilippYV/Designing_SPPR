import math
import pandas as pd
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

    data_pd = pd.DataFrame(data=data, columns=['first_criterion', 'second_criterion'])
    answers_pd = pd.DataFrame(data=answers, columns=['answer'])
    return data_pd, answers_pd

if __name__ == '__main__':
    x, y = generate_data()
    print(x)
    print(y)
