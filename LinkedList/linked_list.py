class Node:
    def __init__(self,_val=None, _next=None):
        self.val = _val
        self.next = _next


class LinkedList:
    def __init__(self):
        self.head = None

    # duplicated are allowed
    def add(self, v):
        n = Node(_val=v)
        if self.head == None:
            self.head = n
            return self.head

        t = self.head
        while t.next != None:
            t = t.next

        t.next = n

    def remove(self, v):
        while self.head.val == v:
            h = self.head
            self.head = self.head.next
            del h

        t = self.head.next
        prev = self.head
        while t != None:
            if t.val == v:
                prev.next = t.next
                del t
                t = prev.next
            prev = t
            t = t.next

    def print(self):
        t = self.head
        while t != None:
            print(f"-> {t.val}", end="")
            t = t.next
        print()
def test():
    ll = LinkedList()

    r = range(10)
    for i in r:
        ll.add(0)
    for i in r:
        ll.add(i)
    for i in r:
        ll.add(i)
    ll.print()
    ll.remove(8)
    ll.print()
    ll.remove(0)
    ll.print()


if __name__ == '__main__':
    test()
