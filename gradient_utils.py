from pandas import DataFrame
import numpy as np

max_iter = 100000
pas = 0.0005

def cleaning(data:DataFrame, columns):
    cleaned = np.array(data.values[:,columns], dtype=float)
    houses = np.array(data.loc[:,"Hogwarts House"])
    return cleaned, houses

def michelling(data:DataFrame):
    for i in range(len(data)):
        data[i] = (data[i] - data.mean())/data.std()

def sigmoise(x):
    return 1 / (1 + np.exp(-x))