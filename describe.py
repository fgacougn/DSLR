from load_csv import load
import sys
from pandas import DataFrame
from stats_utils import stats
import numpy as np
from sortingHat_utils import get_colnums

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
    print(data)
    colnum = get_colnums(data)
    datastats = np.zeros((len(colnum),12))
    print(datastats)
    print(colnum)
    j = 0
    colnames = []
    for i in colnum:
        print(data[data.columns[i]])
        temp = list(data[data.columns[i]])
        datastats[j] = stats([x for x in temp if x == x])
        print(datastats[j])
        colnames.append(data.columns[i])
        j+=1
    datastats = np.transpose(datastats)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    df = DataFrame(datastats,columns=colnames)
    df.index = ["Count","Mean","Std","Min","1%","10%","25%","50%","75%","90%","99%","Max"]
    print(df)




if __name__ == '__main__':
    main(sys.argv, len(sys.argv))