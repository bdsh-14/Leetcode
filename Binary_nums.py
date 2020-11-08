"""
return binary numbers in the form of strings from 1 up to n

n = 3
result = ["1","10","11"]

"""

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


def find_bin(number):
    result = []
    queue = Queue()
    queue.enqueue(1)
    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)
 
    print(result)

find_bin(3)


