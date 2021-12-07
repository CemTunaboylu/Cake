from pars import Stack

class MaxStack:
    def __init__(self):
        self.main, self.tracker = Stack(), Stack()

    def push(self, elm):
        if self.main.size == 0:
            self.tracker.push(elm)
            self.main.push(elm)
            return
        m = max(elm, self.tracker.top.data)
        self.tracker.push(m)
        self.main.push(elm)

    def pop(self):
        if self.main.size != 0:
            self.tracker.pop()
            return self.main.pop()

    def max(self):
        return self.tracker.top.data


def test():
    m_s = MaxStack()
    elms = [4, 2, 14, 1, 18]

    for e in elms:
        m_s.push(e)
        print(f"Stack: {m_s.main.print()}, tracker: {m_s.tracker.print()}")

test()
