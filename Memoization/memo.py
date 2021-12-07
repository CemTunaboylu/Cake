def fib(n):
    if n<0:
        raise IndexError( "There is no such things as a negative index in a series" )
    elif n in [0,1]:
        return n
    print(f"Computing fib({n})")
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    f = fib(10)
