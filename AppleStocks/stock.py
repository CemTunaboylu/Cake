
def best_trade(prices):
    if len(prices) <= 1:
        return 0

    locals =  [] if prices[0] > prices[1] else [prices[0]]
    l = len(prices)
    acc = prices[1] - prices[0]
    for p in range(2, l):
        prev_acc = acc
        acc = prices[p] - prices[p-1]
        d = acc - prev_acc
        if (prev_acc < 0 and acc > 0) or (prev_acc > 0 and acc < 0):
            #local minima or local maxima
            locals.append(prices[p-1])

    locals.append(prices[-1])

    # without shorting -> shorting makes it easier actually find the biggest and smallest and that is it
    l = len(locals)
    if l == 1:
        return -1
    elif l ==  2:
        return 0 if locals[0] == locals[1] else locals[1]-locals[0] # price decreased

    min_elm = min(locals[0], locals[1])
    diff = 0

    for i in range(1, l):
        e = locals[i]
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
    test([1,3,6,9,19])
    test([9,19])
