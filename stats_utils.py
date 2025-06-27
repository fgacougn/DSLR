from pandas import to_numeric, DataFrame
import numpy as np

def stats(column):
    """
    Get stats
    Names of return variable are self explaining
    """
    Count = int(len(column))
    Sum = sum(column)
    Mean = Sum/Count
    Std = (sum((xi - Mean) ** 2 for xi in column) / Count)**0.5
    column.sort()
    Min = column[0]
    p1 = column[int(Count/100) -1]
    p10 = column[int(Count/10) -1]
    q1 = column[int(Count/4) -1]
    q2 = column[int(Count/2) - 1]
    q3 = column[int((3 * Count)/4) -1]
    p90 = column[int((9*Count)/10) -1]
    p99 = column[int((99*Count)/100) -1]
    Max = column[Count - 1]
    return Count,Mean,Std,Min,p1,p10,q1,q2,q3,p90,p99,Max

def stats_small(column):
    """
    Get stats
    Names of return variable are self explaining
    """
    Count = int(len(column))
    column.sort()
    Min = column[0]
    Max = column[Count - 1]
    return Count,Min,Max


def collapse_mean(data, colnum):
    dattarray = np.array(data)
    Means = [data[0][0]]
    for i in colnum:
        clean = [x for x in dattarray[:,i] if x == x]
        Means.append(sum(clean)/ len(clean))
    return Means

def get_full_stats(data:DataFrame):
    (colnum, colnames) = get_colnums(data)
    datastats = np.zeros((len(colnum),12))
    j = 0
    for i in colnum:
        temp = list(data[data.columns[i]])
        datastats[j] = stats([x for x in temp if x == x])
        j+=1
    datastats = np.transpose(datastats)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    df = DataFrame(datastats,columns=colnames)
    df.index = ["Count","Mean","Std","Min","1%","10%","25%","50%","75%","90%","99%","Max"]
    return df

def get_small_stats(data:DataFrame):
    (colnum, colnames) = get_colnums(data)
    datastats = np.zeros((len(colnum),3))
    j = 0
    for i in colnum:
        temp = list(data[data.columns[i]])
        datastats[j] = stats_small([x for x in temp if x == x])
        j+=1
    datastats = np.transpose(datastats)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    df = DataFrame(datastats,columns=colnames)
    df.index = ["Count","Min","Max"]
    return df


def get_colnums(data):
    colnum = []
    colnames = []
    for i in range(len(data.columns)):
        try :
            to_numeric(data[data.columns[i]])
            colnum.append(i)
            colnames.append(data.columns[i])
        except ValueError:
            print(end="")
    return colnum, colnames