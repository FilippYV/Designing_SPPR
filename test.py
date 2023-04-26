import random
import pandas as pd
import numpy as np
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/DLSchool/dlschool_old/master/materials/homeworks/hw04/data/apples_pears.csv")
data.head(10)

X = data.iloc[:,:2].values  # матрица объекты-признаки
y = data['target'].values.reshape((-1, 1))  # классы (столбец из нулей и единиц)

x1 = X[:, 0]
x2 = X[:, 1]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
np.random.seed(62)
w1 = np.random.randn(1)
w2 = np.random.randn(1)
w0 = np.random.randn(1)

print(w1, w2, w0)

# form range 0..999
idx = np.arange(1000)

# random shuffling
np.random.shuffle(idx)
x1, x2, y = x1[idx], x2[idx], y[idx]
# learning rate
lr = 0.001
print(y, 'y')

# number of epochs
n_epochs = 10000

for epoch in range(n_epochs):
    i = random.randint(0, 999)

    yhat = w1 * x1[i] + w2 * x2[i] + w0

    w1_grad = -((y[i] - sigmoid(yhat)) * x1[i])

    w2_grad = -((y[i] - sigmoid(yhat)) * x2[i])

    w0_grad = -(y[i] - sigmoid(yhat))

    w1 -= lr * w1_grad

    w2 -= lr * w2_grad

    w0 -= lr * w0_grad

print(w1, w2, w0)