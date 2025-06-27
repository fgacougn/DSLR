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
    Q1 = column[int(Count/4) -1]
    Q2 = column[int(Count/2) - 1]
    Q3 = column[int(3 * Count/4) -1]
    Max = column[Count - 1]
    return Count,Mean,Std,Min,Q1,Q2,Q3,Max
