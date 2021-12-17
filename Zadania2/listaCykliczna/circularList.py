class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, element, index):
        if index > self.length or index < 0:
            return "Nie mozna dodac elementu"
        else:
            if index == 0:
                element.next = self.head
                if element.next is None:
                    element.next = element
                self.head = element
            else:
                temp = self.head
                for _ in range(0,index):
                    temp = temp.next
                if temp is not None:
                    element.next = temp
                else:
                    element.next = self.head
                temp = self.head
                for _ in range(0, index-1):
                    temp = temp.next
                temp.next = element
            self.length += 1

    def remove(self, index):
        if index > self.length - 1 or index < 0:
            return 1    
        if index == 0:
            if self.length == 1:
                self.head = None 
            else:
                self.head = self.head.next
                last = self.head
                for _ in range(self.length - 1):
                    last = last.next 
                last.next = self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
        self.length -= 1
        

    def find(self, value):
        if self.length == 0: 
            return "Nie ma takiej wartosci"
        if self.head.value == value:
            return "Podana wartosc znajduje sie na liscie"
        temp = self.head.next
        if temp is not None:
            while temp is not self.head:
                    if temp.value == value:
                        return "Podana wartosc znajduje sie na liscie"
                    temp = temp.next
        return "Nie ma takiej wartosci"


    def print(self):
        temp = self.head
        if temp is None: 
            print("Lista jest pusta")
        else:
            print(temp.value)
            temp = temp.next
            if temp is not None:
                while temp is not self.head:
                    print(temp.value)
                    temp = temp.next

    

i1 = Item(1)
i2 = Item(2)
i3 = Item(3)
i4 = Item(4)

cList = CircularList()
cList.add(i1, 0)
cList.print()
cList.add(i2, 1)
cList.print()
cList.add(i3, 2)
cList.print()
cList.add(i4, 3)
cList.print()
cList.remove(2)
cList.print()
print(cList.find(6))
print(cList.find(2))