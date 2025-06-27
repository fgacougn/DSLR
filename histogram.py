from load_csv import load
from sortingHat_utils import get_colnums
from stats_utils import collapse_mean

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
    Ravenclaw = []
    Slitherin = []
    Hufflepuff = []
    Gryffindor = []
    for i in data.values :
        # print(i)
        match i[0]:
            case "Ravenclaw":
                Ravenclaw.append(i)
            case "Slitherin":
                Slitherin.append(i)
            case "Hufflepuff":
                Hufflepuff.append(i)
            case "Gryffindor":
                Gryffindor.append(i)
    print ("Ravenclaw\n", Ravenclaw)
    print ("Slitherin\n", Slitherin)
    print ("Hufflepuff\n", Hufflepuff)
    print ("Gryffindor\n", Gryffindor)
    colnums = get_colnums(data)
    RavenclawM = collapse_mean(Ravenclaw, colnums)
    SlitherinM = collapse_mean(Slitherin, colnums)
    HufflepuffM = collapse_mean(Hufflepuff, colnums)
    GryffindorM = collapse_mean(Gryffindor, colnums)



if __name__ == '__main__':
    main([0,"datasets/dataset_train.csv"],2)