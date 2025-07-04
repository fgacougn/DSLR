from load_csv import load
import numpy as np 
from pandas import DataFrame
import gradient_utils as gu
from gradient_descent import gradient_batch

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
    dataTrain, houses=gu.cleaning(data,[6,8,9,11,13,17])
    np.apply_along_axis(gu.michelling, 0, dataTrain)
    sorting_hat = DataFrame(gradient_batch(dataTrain,houses), columns=["Houses",6,8,9,11,13,17])
    sorting_hat.to_csv("datasets/ticouvre_hairline.csv", index=False)


if __name__ == '__main__':
    main([0,"datasets/dataset_train.csv"],2)
