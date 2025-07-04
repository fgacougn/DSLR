from load_csv import load
import numpy as np
from pandas import DataFrame
import gradient_utils as gu
import sys


def predict(data, weigths: DataFrame) -> DataFrame:
    np.apply_along_axis(gu.michelling, 0, data)
    print(data)
    houses = []
    l_index = 0
    for j in data:
        max = -555555
        house = "Prout"
        for k in range(len(weigths.index)):
            fitness = 0
            fitness2 = j.dot(np.array(weigths.values[k]).T)
            for i in range(len(weigths.columns)):
                fitness += weigths.values[k][i] * j[i]
            print(fitness, fitness2)
            fitness = gu.sigmoise(fitness)
            print(fitness, weigths.index[k])
            if fitness > max:
                house = weigths.index[k]
                max = fitness
        print(max, fitness, house)
        houses.append([l_index, house])
        l_index += 1
    return houses


def main(argv, argc):
    """
    Affiching the dataset passing in argument
    """
    if argc < 2:
        print("Not enough d'arguments")
        return
    if argc < 3:
        weight = load("datasets/ticouvre_hairline2.csv")
    else:
        weight = load(argv[2])
    if (weight is None):
        print("No weightset")
        return
    data = load(argv[1])
    if (data is None):
        print("No dataset")
        return
    print(data)
    print(weight)
    data = data.fillna(0)
    print(gu.cleaning(data, gu.selected_courses))
    res = DataFrame(predict(gu.cleaning(data, gu.selected_courses)[0], weight), columns=["Index", "Hogwarts House"])
    res.to_csv("houses.csv", index=False)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
