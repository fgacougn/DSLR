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
