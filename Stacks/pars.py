counter_party = {
    "}": "{",
    "]":"[",
    ")":"(",
}

class Node:
    def __init__(self, _d, _b = None):
        self.data = _d
        self.before = _b


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, elm):
        e = Node(elm, self.top)
        self.top = e
        self.size +=1

    def pop(self):
        if not self.top:
            return None
        e = self.top
        self.top = self.top.before
        self.size -= 1
        return e

    def check(self, elm):
        if not self.top:
            return False
        return self.top.data == elm

def test(sample, res):
    s = Stack()
    elms = "{}[]()"
    for sam in sample:
        if sam not in elms:
            continue
        if sam in counter_party.keys():
            c_p = counter_party[sam]
            if s.check(c_p):
                s.pop()
            else:
                s.push(sam) #I am inserting because ]}) can come at first, in this case stack size will be 0
                break
        else:
            s.push(sam)

    assert (s.size == 0) == res

if __name__ == '__main__':
    test("{ [ ] ( ) }", True)
    test("{ [ ( ] ) }", False)
    test("{]}", False)
    test("{", False)
    test("]", False)
