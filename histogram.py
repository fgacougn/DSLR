from load_csv import load
from sortingHat_utils import get_mean_by_House, oneline_onegrade
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
    df = get_mean_by_House(data)
    dataWide = oneline_onegrade(data)
    print(dataWide)
    # g = sns.FacetGrid(data, col = "Hogwarts House")
    # g.map_dataframe(sns.histplot,x="Arithmancy", y = "Hogwarts House", hue = "Hogwarts House")
    # g = sns.FacetGrid(dataWide, col = "Course", row = "Hogwarts House")
    g = sns.FacetGrid(dataWide, col = "Course")
    g.map_dataframe(sns.histplot,x="Grade",hue = "Hogwarts House", element="step")
    plt.show()


if __name__ == '__main__':
    main([0,"datasets/dataset_train.csv"],2)