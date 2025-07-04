from load_csv import load
from sortingHat_utils import oneline_onedif_to_transfiguration, oneline_onedif_to_Astronomy
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
    dataWide = oneline_onedif_to_transfiguration(data)
    g = sns.FacetGrid(dataWide, col="Course", hue="Hogwarts House", palette=['tab:blue', 'tab:green', 'tab:orange', 'tab:red'])
    g.map_dataframe(sns.scatterplot, x="Grade", y="Diff to transfiguration")
    g.add_legend(title="Houses")
    dataWide = oneline_onedif_to_Astronomy(data)
    h = sns.FacetGrid(dataWide, col="Course", hue="Hogwarts House", palette=['tab:blue', 'tab:green', 'tab:orange', 'tab:red'])
    h.map_dataframe(sns.scatterplot, x="Grade", y="Diff to transfiguration")
    h.add_legend(title="Houses")
    plt.show()


if __name__ == '__main__':
    main([0, "datasets/dataset_train.csv"], 2)
