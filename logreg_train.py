from load_csv import load
import numpy as np 
from pandas import DataFrame
import gradient_utils as gu
from sortingHat_utils import normalize_grades
from gradient_descent import gradient_batch, gradient_unit, gradient_mini_batch, gradient_stochas

def main(argv, argc):
    """
    Affiching the dataset passing in argument
    """
    if argc < 2:
        print("Not enough d'arguments")
        return
    data = load(argv[1])
    if (data is None):
        print("No dataset")
        return
    data = data.dropna()
    dataTrain, houses=gu.cleaning(data,gu.selected_courses)
    np.apply_along_axis(gu.michelling, 0, dataTrain)
    # sorting_hat = DataFrame(gradient_unit(dataTrain,houses), columns=gu.columns)
    # sorting_hat.to_csv("datasets/ticouvre_hairline0.csv", index=False)
    sorting_hat = DataFrame(gradient_mini_batch(dataTrain,houses), columns=gu.columns)
    sorting_hat.to_csv("datasets/ticouvre_hairline1.csv", index=False)
    sorting_hat = DataFrame(gradient_batch(dataTrain,houses), columns=gu.columns)
    sorting_hat.to_csv("datasets/ticouvre_hairline2.csv", index=False)
    sorting_hat = DataFrame(gradient_stochas(dataTrain,houses), columns=gu.columns)
    sorting_hat.to_csv("datasets/ticouvre_hairline3.csv", index=False)


if __name__ == '__main__':
    main([0,"datasets/dataset_train.csv"],2)
