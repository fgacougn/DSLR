from pandas import read_csv
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """
    Charge un dataset et le renvoie
    None si impossible a charger
    """
    try:
        ds = read_csv(path, index_col=0)
    except FileNotFoundError:
        return None
    print("Loading dataset of dimensions", ds.shape)
    return ds
