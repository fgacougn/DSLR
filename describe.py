from load_csv import load
import sys
from pandas import to_numeric
from stats_utils import stats
import numpy as np

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
    colnum = []
    for i in range(len(data.columns)):
        try :
            print(to_numeric(data[data.columns[i]]))
            colnum.append(i)
        except ValueError:
            print(end="")
    datastats = np.zeros((len(colnum),8))
    print(datastats)
    print(colnum)
    j = 0
    for i in colnum:
        print(data[data.columns[i]])
        temp = list(data[data.columns[i]])
        datastats[j] = stats([x for x in temp if x == x])
        print(datastats[j])
        j+=1
    datastats = np.transpose(datastats)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    print(datastats)



if __name__ == '__main__':
    main(sys.argv, len(sys.argv))