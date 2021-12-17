class Queue:
    def __init__(self, length):
        self.items = []
        self.length = length

    def enqueue(self, item):
        if self.isFull():
            print('kolejka jest pelna')
        else:
            self.items.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            print('kolejka jest pusta')
        else:
            self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def isFull(self):
        return len(self.items) >= self.length


queue = Queue(3)
print(queue.isEmpty())
print(queue.size())
queue.enqueue(4)
queue.enqueue(1)
queue.enqueue(6)
queue.enqueue(5)
print(queue.size())
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.size())
print(queue.isEmpty())

