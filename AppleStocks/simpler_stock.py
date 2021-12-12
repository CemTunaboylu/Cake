
def best_trade(prices):
    l = len(prices)
    if l <= 1:
        raise ValueError("Price array should be longer than 1")


    min_elm = prices[0]
    diff = prices[1] - prices[0]

    for i in range(1, l):
        e = prices[i]
        if min_elm > e:
            min_elm = e
            continue
        d = e - min_elm
        if d > diff:
            diff = d

    return diff

def test(p = [10, 7, 5, 8, 11, 9]):
    print(f"Testing for {p}")
    r = best_trade(p)
    print(f"Result : {r}")

if __name__ == '__main__':
    test()
    test([5,9,5,3,8,7,6,5,7,3])
    test([9,5,3,8,7,6,5,7,3])
    test([1,1,1,1,1,1,1])
    test([10,9,8,5,3])
    test([10,8,6,5,3])
    test([10,8,8,5,3])
    test([1,3,6,9,19])
    test([9,19])
    test([29,19])
