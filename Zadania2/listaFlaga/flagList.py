class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


class FlagList:
    def __init__(self):
        self.flag = Item(None)
        self.head = self.flag
        self.length = 0

    def add(self, element, index):
        if index > self.length or index < 0:
            return 1
        if index == 0:
            element.next = self.flag.next
            self.flag.next = element
        if index == self.length:
            element.next = self.flag
            temp = self.flag
            for _ in range(index):
                temp = temp.next
            temp.next = element
        elif index != 0:
            temp = self.flag
            for _ in range(index + 1):
                temp = temp.next
            element.next = temp
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.next = element
        self.length += 1

    
    def remove(self, index):
        if index > self.length or index < 0:
            return 1    
        prev = self.flag
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        if prev.next is None:
            prev.next = self.flag
        self.length -= 1


    def find(self, value):
        self.flag.value = value
        temp = self.flag.next
        if temp is not None:
            while temp.value != value:
                temp = temp.next
            if temp is not self.flag:
                print("Istnieje element z podana wartoscia na liscie")
                self.flag.value = None
                return 0
        print("Nie ma takiego elementu")
        self.flag.value = None

    def print(self):
        temp = self.flag.next
        if temp is not None:
            while temp is not self.flag:
                print(temp.value)
                temp = temp.next


i1 = Item(1)
i2 = Item(2)
i3 = Item(3)
i4 = Item(4)

fList = FlagList()
fList.add(i1, 0)
fList.print()
fList.add(i2, 1)
fList.print()
fList.add(i3, 2)
fList.print()
fList.add(i4, 3)
fList.print()
fList.remove(2)
fList.print()
fList.find(6)
fList.find(4)
