class Conversion:
    def __init__(self):
        self.items = []  # stos operatorow
        self.operators = {
            "(": 0,
            "+": 1,
            "-": 1,
            ")": 1,
            "*": 2,
            "/": 2,
            "%": 2,
            "^": 3
        }
        self.output = []  # wyjscie

    def is_empty(self):
        return self.items == []

    def push(self, item):
        is_operator = False

        for operator in self.operators:  
            if item == operator:
                is_operator = True

        if is_operator:
            n1 = self.peek()
            self.pop()
            n2 = self.peek()
            self.pop()
            self.items.append(n2 + item + n1)
        else:
            self.items.append(item)


    def pop(self):
        self.items.pop()

    def erase(self):
        self.items = []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        print('Wyjscie')
        for item in self.output:
            print(item, end=' ')
        print('')
        print('Operatory: ')
        for item in self.items:
            print(item, end=' ')
        print('')


s = Conversion()
while True:
    cos = input()
    s.push(cos)
    s.print()
