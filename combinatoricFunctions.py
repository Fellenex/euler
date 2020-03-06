factMemos = dict()
factMemos[0] = 1.0
factMemos[1] = 1.0

def memoizedFactorial(_n):
    try:
        return(factMemos[_n])
    except KeyError:
        new = _n*memoizedFactorial(_n-1)
        factMemos[_n] = new
        return(new)


#Returns n choose r
def nCr(_n, _r):
    if _n < _r: return(0.0)

    if _n in factMemos: memoN = factMemos[_n]
    else: memoN = memoizedFactorial(_n)

    if _r in factMemos: memoR = factMemos[_r]
    else: memoR = memoizedFactorial(_r)

    if _n - _r in factMemos: memoD = factMemos[_n - _r]
    else: memoD = memoizedFactorial(_n - _r)

    return (memoN / (memoR * memoD))
