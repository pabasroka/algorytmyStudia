class Item:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

class Pqueue:
    def __init__(self, length):
        self.items = []
        self.length = length

    def enqueue(self, item, priority):
        item = Item(item, priority)
        if self.isFull():
            print('kolejka jest pelna')
        else:
            if self.size() == 0:
                self.items.append(item)
                return
            else:
                for i in range(0, self.size()):
                    if item.priority <= self.items[i].priority:
                        if self.isFull():
                            del self.items[(self.length - 1)]
                        if i == (self.length - 1):
                            del self.items[i]
                            self.items.insert(i, item)
                            break
                        else:
                            self.items.insert(i, item)
                            break
                    elif i == (self.size() - 1) and self.size() <= self.length - 1 and self.items[i].priority < item.priority:
                        if self.size() == self.length - 1:
                            del self.items[self.length - 1]
                        self.items.insert(i + 1, item)
                        break

    def dequeue(self):
        if self.isEmpty():
            print('kolejka jest pusta')
        else:
            self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def isFull(self):
        return len(self.items) >= self.length


queue = Pqueue(3)
print(queue.isEmpty())
print(queue.size())
queue.enqueue('paba', 3)
queue.enqueue('sroka', 1)
queue.enqueue('mati', 2)
queue.dequeue()
print(queue.size())
queue.dequeue()
print(queue.size())
print(queue.isEmpty())

