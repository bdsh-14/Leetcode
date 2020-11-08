# Search 

class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_tail(self, val):
        temp = ListNode(val)
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = temp
    
    def search(self, val):
        temp = ListNode(val)
        
        current = self.head
        while current:
            if current.val == temp.val:
                print(True)
                return True
            current = current.next
        return False
    

lst = LinkedList()
lst.insert_at_tail(5)
lst.insert_at_tail(90)
lst.insert_at_tail(10)
lst.insert_at_tail(4)

lst.search(4)

