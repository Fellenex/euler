#Getting math overflow errors using math.pow
def myPow(_base, _pow):
    if _pow == 0:
        return(1)
    else:
        p = _pow
        r = _base
        while p > 1:
            r *= _base
            p -=1
        return(r)
