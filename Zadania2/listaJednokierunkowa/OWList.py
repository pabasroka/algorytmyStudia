class Item:
    def __init__(self, value):
        self.value = value
        self.next = None

class OWList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add(self, element, index):
        if index < 0 or index > self.length:
            print('Nie mozna dodac elementu')
            return
        if index == 0:
            element.next = self.head
            self.head = element
        else:
            temp = self.head
            for i in range(0, index):
                temp = temp.next
            element.next = temp
            temp = self.head
            for i in range(0, index - 1):
                temp = temp.next
            temp.next = element
        self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            print("Nie mozna usunac elementu")
            return
        if index == 0:
            self.head = self.head.next
        else:
            previous = self.head
            for i in range(index - 1):
                previous = previous.next
            previous.next = previous.next.next
        self.length -= 1

    def size(self):
        i = 0
        temp = self.head
        while temp is not None:
            i += 1
            temp = temp.next
        return i

    def find(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                print("Value ", value, " index: ", temp)
                return
            else:
                temp = temp.next
        print("Nie ma takiej wartosci w liscie")
        return

    def print(self):
        temp = self.head
        if temp is None:
            print('Lista jest pusta')
        else:
            while(temp is not None):
                print(temp.value, end="")
                temp = temp.next
            print("\n")

i1 = Item(1)
i2 = Item(2)
i3 = Item(3)
i4 = Item(4)

owlist = OWList()
owlist.add(i1, 0)
owlist.print()
owlist.add(i2, 1)
owlist.print()
owlist.add(i3, 2)
owlist.print()
owlist.add(i4, 3)
owlist.print()
owlist.remove(2)
owlist.print()
owlist.find(6)
owlist.find(4)
print(owlist.size())
