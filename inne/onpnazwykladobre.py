def czyoperator(a):

    if(a == '*' or a == '+' or a == '/' or a == '-' or a == '^'):
        return 1
    else:
        return 0


class Stack:

    def __init__(self):        # Kostruktor
        self.Stack = []

    def Push(self, s):      # Dodawanie elementów
        self.Stack.append(s)

    def Pop(self):          # Usuwanie elementu
        self.Stack.pop(len(self.Stack)-1)

    def Size(self):         # Ilość elementów na stosie
        return len(self.Stack)

    def Top(self):          # Zwraca ostatni element
        return self.Stack[len(self.Stack)-1]

    def Empty(self):        # Sprawdza czy stos jest pusty
        if len(self.Stack) == 0:
            return True
        else:
            return False


stos = Stack()

wyraz = '40 50 6 3 / - 1 + 2 ^ *'
i = 0

p = 0
while p == 0:
    if wyraz[i] == " ":
        i = i+1
    w = czyoperator(wyraz[i])

    if w == 0:
        g = wyraz[i]
        if wyraz[i+1] != " ":
            while wyraz[i+1] != " ":
                g = g+wyraz[i+1]
                i = i+1

        stos.Push(g)

    else:

        b = stos.Top()
        stos.Pop()
        c = stos.Top()
        stos.Pop()
        d = '('+c+wyraz[i]+b+')'
        stos.Push(d)

    i = i+1
    z = len(wyraz)
    if(i == z):
        p = 1


print(stos.Top())
