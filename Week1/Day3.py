# 203. use dummy node return dummy.next

# 707. curr.next = ListNode(val, curr.next)
# addAtIndex 注意区间 多练习
class ListNode(object):

    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.dummy_head = ListNode(0, None)
        self.size = 0
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy_head.next
        for i in range(index):
            curr = curr.next
        #self.printList()
        return curr.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1
        #self.printList()
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        curr = self.dummy_head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val, None)
        self.size += 1
        # self.printList()
        
        
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        curr = self.dummy_head
        for i in range(index):
            curr = curr.next
        curr.next = ListNode(val, curr.next)
        self.size += 1
        # self.printList()
        
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        curr = self.dummy_head
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1
        #self.printList()
    
    def printList(self):
        curr = self.dummy_head
        while curr:
            print(curr.val)
            curr = curr.next
        print("___")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# 206. two cursors
# pre -> cur -> next
# save curr.next as tmp
# pre <- cur
# pre move to cur
# cur move to tmp