import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree

datas = [
            [1, 0],
            [1, 0],
            [1, 0],
            [0, 1],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1]]
data = pd.DataFrame(data=datas, columns=['первый критерий', 'второй критерий'])
print(data)