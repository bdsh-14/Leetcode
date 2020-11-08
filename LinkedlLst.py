# singly linkedList

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None # pointer to the first node

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_head(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        return self.head

    def insert_at_tail(self, val):
        temp = Node(val)
        if self.is_empty:
            self.head = temp
        current = self.head 
        while current.next != None:
            current = current.next
        current.next = temp



lst = LinkedList()
print(lst.is_empty())

lst.insert_at_head(10)
lst.insert_at_head(20)
lst.insert_at_head(30)

lst.insert_at_tail(100)



print(str(lst.head.next.next.next.data))
