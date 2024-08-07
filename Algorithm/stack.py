# STACK implementation
class Stack:
    def __init__(self):
        # initialize the stack - list
        self.item = []

    def is_empty(self):
        return not len(self.item)

    def push(self, val):
        self.item.append(val)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def __str__(self):
        return str(self.item)


if __name__ == '__main__':
    s = Stack()
    print(s.push(4))
    s.push(5)
    s.push(6)
    s.pop()
    print(s.peek())
    print(s)

