# There are lots of ways to fix this. We can use a list but there is an amorthized cost, when we hit the capacity of the list, a new one will be created with double the size, and all the elements will be
# inserted to it, this is O(N). We can use a dictionary for O(1) time operations.



class Fi:
    def __init__(self):
        self.memo = { 0:0, 1:1 }

    def calc(self, nth):
        if nth<0:
            raise IndexError( "There is no such things as a negative index in a series" )
        if nth in self.memo:
            return self.memo[nth]

        return self.fib(nth)
    def fib(self, n):
        if n in [0,1]:
            return self.memo[n]
        if n in self.memo:
            return self.memo[n]
        print(f"Computing fib({n})")
        f = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = f
        return f



if __name__ == '__main__':
    fi = Fi()
    f = fi.calc(10)
    print(f)
    print(fi.memo)
