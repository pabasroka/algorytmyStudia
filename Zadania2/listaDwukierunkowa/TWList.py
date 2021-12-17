class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class TWOList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, el, index):
        if index > self.length or index < 0:
            return False
        temp = self.head
        if temp is None:
            self.head = el
            self.tail = el
        else:
            for _ in range(0, index):
                temp = temp.next
            if temp is None:
                el.prev = self.tail
                self.tail.next = el
                self.tail = el
            elif temp.prev is not None:
                temp.prev.next = el
                el.prev = temp.prev
                el.next = temp
                temp.prev = el
            else:
                el.next = self.head
                self.head = el
                temp.prev = el
        self.length += 1
        return True
            
    def remove(self, index):
        if index > self.length - 1 or index < 0:
            return 1 
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        if temp.next is not None:
            if temp.prev is not None:
                temp.prev.next = temp.next
            else:
                self.head = temp.next    
            temp.next.prev = temp.prev
        else:
            if temp.prev is not None:
                temp.prev.next = temp.next 
            else:
                self.head = None
            self.tail = temp.prev
        self.length -= 1

    def print(self, reversed=False):
        if not reversed:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
        else:
            temp = self.tail
            while temp is not None:
                print(temp.value)
                temp = temp.prev

    def find(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return 0
            else:
                temp = temp.next


i1 = Item(1)
i2 = Item(2)
i3 = Item(3)
i4 = Item(4)

twolist = TWOList()
twolist.add(i1, 0)
twolist.print()
print("===")
twolist.add(i2, 1)
twolist.print()
print("===")
twolist.add(i3, 2)
twolist.print()
print("===")
twolist.add(i4, 3)
twolist.print()
twolist.print(True)
print("===")
twolist.remove(2)
twolist.print()
print("===")
twolist.find(6)
twolist.find(4)