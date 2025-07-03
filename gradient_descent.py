def to_max(coefs:list[float]):
    ret = 0
    for i in coefs:
        ret += i**2 if i >= 0 else - i**2
    return ret

def grads(coefs:list[float]):
    return 2*coefs