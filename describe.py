from load_csv import load
import sys
from stats_utils import get_full_stats

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
    
    
    print(get_full_stats(data))




if __name__ == '__main__':
    main(sys.argv, len(sys.argv))