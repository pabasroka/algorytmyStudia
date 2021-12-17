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
        if item == "nil":
            self.output.extend(reversed(self.items))
            self.erase()
            return

        is_operator = False
        for operator in self.operators:  # dla kazdego operatora z dictionary
            if item == operator:  # jesli input jest operatorem
                is_operator = True

        if is_operator:
            if self.is_empty() or item == "(":
                self.items.append(item)  # jesli stos jest pusty umieszczamy operator na stosie
            elif item == ")":
                for oper in self.items:
                    if oper == "(":
                        self.items.pop()
                        break
                    else:
                        self.output.append(self.peek())
                        self.items.pop()
            elif self.operators[self.peek()] < self.operators[item]:  # jezeli ostatni operator ma nizszy priorytet od pobranego
                self.items.append(item)
            elif self.operators[self.peek()] >= self.operators[item]:
                for oper in self.items:
                    if self.operators[oper] >= self.operators[item]:
                        self.output.append(self.peek())
                        self.items.pop()
                self.items.append(item)  # umieszczamy wczytany z wyrazenia operator na stosie
        else:
            self.output.append(item)

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
