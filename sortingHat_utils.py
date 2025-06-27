from pandas import to_numeric
from stats_utils import collapse_mean, get_colnums, get_small_stats
from pandas import DataFrame


def get_mean_by_House(data):
    Ravenclaw = []
    Slytherin = []
    Hufflepuff = []
    Gryffindor = []
    for i in data.values :
        # print(i)
        match i[0]:
            case "Ravenclaw":
                Ravenclaw.append(i)
            case "Slytherin":
                Slytherin.append(i)
            case "Hufflepuff":
                Hufflepuff.append(i)
            case "Gryffindor":
                Gryffindor.append(i)
    # print ("Ravenclaw\n", Ravenclaw)
    # print ("Slytherin\n", Slytherin)
    # print ("Hufflepuff\n", Hufflepuff)
    # print ("Gryffindor\n", Gryffindor)
    (colnums, colnames )= get_colnums(data)
    RavenclawM = collapse_mean(Ravenclaw, colnums)
    SlytherinM = collapse_mean(Slytherin, colnums)
    HufflepuffM = collapse_mean(Hufflepuff, colnums)
    GryffindorM = collapse_mean(Gryffindor, colnums)
    df = DataFrame([RavenclawM,SlytherinM,HufflepuffM,GryffindorM],columns=["Hogwarts House"] + colnames)
    df.index = ["Ravenclaw","Slytherin","Hufflepuff","Gryffindor"]
    return df

def oneline_onegrade(data:DataFrame):
    newdata = []
    small_stats = get_small_stats(data)
    print("smallstats\n",small_stats.values[0][0],"\n", small_stats)
    (colnum, colname) = get_colnums(data)
    print (data.columns)
    for i in data.values :
        k = 0
        for j in colnum:
            if(round(100 *(i[j] - small_stats.values[1][k]) / abs(small_stats.values[2][k]- small_stats.values[1][k]),0) > 100):
                print (i[j], small_stats.values[1][k],abs(small_stats.values[2][k]- small_stats.values[1][k]) ,  100 *(i[j] - small_stats.values[1][k]) / abs(small_stats.values[2][k]- small_stats.values[1][k]))
                raise ValueError
            newdata.append([i[0],data.columns[j],100 *(i[j] - small_stats.values[1][k]) / abs(small_stats.values[2][k]- small_stats.values[1][k])])
            k+=1
    return DataFrame(newdata,columns=["Hogwarts House","Course","Grade"])