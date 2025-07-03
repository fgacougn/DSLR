from load_csv import load
from sortingHat_utils import get_mean_by_House, normalize_grades

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
    data = normalize_grades(data)
    df = get_mean_by_House(data)
    print(df)
    # g = sns.FacetGrid(data, col = "Hogwarts House")
    # g.map_dataframe(sns.histplot,x="Arithmancy", y = "Hogwarts House", hue = "Hogwarts House")
    # g = sns.FacetGrid(dataWide, col = "Course", row = "Hogwarts House")


if __name__ == '__main__':
    main([0,"datasets/dataset_train.csv"],2)