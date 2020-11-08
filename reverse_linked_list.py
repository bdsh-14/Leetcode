

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None


    def insert_at_tail(self, val):
        temp = ListNode(val)
        cur = self.head
        if self.head == None:
            self.head = temp
            return
        while cur.next:
            cur = cur.next
        cur.next = temp
    
    def reverseList(self):
        current = self.head
        prev, next_element = None, None
        while current:
            next_element = current.next
            current.next = prev
            prev = current 
            current = next_element
            
        print(prev.val)

lst = LinkedList()
print(lst.is_empty())


lst.insert_at_tail(100)
lst.insert_at_tail(200)
lst.insert_at_tail(300)
print(str(lst.head.next.val))

lst.reverseList()