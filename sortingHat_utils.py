from pandas import to_numeric


def get_colnums(data):
    colnum = []
    for i in range(len(data.columns)):
        try :
            to_numeric(data[data.columns[i]])
            colnum.append(i)
        except ValueError:
            print(end="")
    return colnum