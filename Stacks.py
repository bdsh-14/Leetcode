class Stack:
    def __init__(self):
        self.stackList = []

    def push(self, val):
        self.stackList.append(val)
    
    def is_empty(self):
        return len(self.stackList) == 0
    
    def top(self):
        if self.is_empty():
            return None
        return self.stackList[-1]
    
    def size(self):
        return len(self.stackList)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stackList.pop()


        

stack = Stack()

for i in range(5):
    stack.push(i)
print("is_empty(): " + str(stack.is_empty()))
print("top(): " + str(stack.top()))
print("size(): " + str(stack.size()))