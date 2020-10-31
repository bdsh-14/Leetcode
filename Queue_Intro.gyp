#Linear queue

class Queue:
    def __init__(self):
        self.queueList = []

    def is_empty(self):
        return len(self.queueList) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queueList[0]

    def back(self):
        if self.is_empty():
            return None
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)


    def enqueue(self, val):
        self.queueList.append(val)
    
    def dequeue(self):
        front = self.front()
        self.queueList.remove(front)
        return front


queue = Queue()


print("queue.enqueue(2);")
queue.enqueue(2)
print("queue.enqueue(4);")
queue.enqueue(4)
print("queue.enqueue(6);")
queue.enqueue(6)
print("queue.enqueue(8);")
queue.enqueue(8)
print("queue.enqueue(10);")
queue.enqueue(10)

print("Dequeue(): " + str(queue.dequeue()))
print("Dequeue(): " + str(queue.dequeue()))

print("front(): " + str(queue.front()))
print("back(): " + str(queue.back()))

queue.enqueue(12)
queue.enqueue(14)

while queue.is_empty() is False:
    print("Dequeue(): " + str(queue.dequeue()))

print("is_empty(): " + str(queue.is_empty()))