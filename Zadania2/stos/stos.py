class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print('stos jest pusty')
        else:
            self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def print(self):
        for item in self.items:
            print(item, end=' ')
        print('')


stack = Stack()
stack.push(5)
stack.print()
print(stack.is_empty())
stack.push(14)
stack.push(-7)
print(stack.peek())
print(stack.size())
stack.pop()
stack.pop()
stack.pop()
print(stack.peek())
print(stack.size())