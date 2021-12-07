from pars import Stack

class Queue:
    def __init__(self):
        self.s1, self.s2 = Stack(), Stack()

    def enqueue(self, elm):
        self.s1.push(elm)

    def dequeue(self):
        if self.s2.size != 0:
            return self.s2.pop()
        else:
            while self.s1.size > 1:
                self.s2.push( self.s1.pop().data )
            return self.s1.pop()


def test():
    r = range(10)
    q = Queue()
    for i in r:
        q.enqueue(i)

    e = q.dequeue()
    for i in range(3):
        e = q.dequeue()
    for i in r:
        q.enqueue(i+10)
    for i in range(7):
        e = q.dequeue()
    print(f"dequeued: {e.data}")
    print(f"s1: {q.s1.print()}, s2: {q.s2.print()}")
if __name__ == '__main__':
    test()
