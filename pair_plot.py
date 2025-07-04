from load_csv import load
from sortingHat_utils import normalize_grades
import seaborn as sns
import matplotlib.pyplot as plt


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
    datanorm = normalize_grades(data)
    print(datanorm)
    g = sns.PairGrid(datanorm, hue="Hogwarts House")
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot)
    g.add_legend()
    plt.show()


if __name__ == '__main__':
    main([0, "datasets/dataset_train.csv"], 2)
