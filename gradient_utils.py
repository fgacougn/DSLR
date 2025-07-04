from pandas import DataFrame
import numpy as np

max_iter = 100000
pas = 0.0005
# selected_courses = [6,8,9,11,13,17]
# columns = ["Houses",6,8,9,11,13,17]
selected_courses = [5,6,7,8,9,10,11,12,13,14,15,16,17]
columns = ["Houses",5,6,7,8,9,10,11,12,13,14,15,16,17]

def cleaning(data:DataFrame, columns):
    cleaned = np.array(data.values[:,columns], dtype=float)
    houses = np.array(data.loc[:,"Hogwarts House"])
    return cleaned, houses

def michelling(data:DataFrame):
    for i in range(len(data)):
        data[i] = (data[i] - data.mean())/data.std()

def sigmoise(x):
    return 1 / (1 + np.exp(-x))