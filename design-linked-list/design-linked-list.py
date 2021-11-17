class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            curr = self.head
            if not index:
                return self.head.val
            else:
                for _ in range(index):
                    curr = curr.next
                return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if not self.size:
            self.addAtHead(val)
        else:
            curr = self.head
            while curr and curr.next:
                curr = curr.next
            curr.next = newNode
            self.size += 1
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif 0 < index < self.size:
            newNode = ListNode(val)
            curr = self.head
            for _ in range(index -1):
                curr = curr.next
            nxt = curr.next
            curr.next = newNode
            curr = curr.next
            curr.next = nxt
            self.size += 1
            
            

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            if not index:
                self.head = self.head.next
            else:
                curr = self.head
                for _ in range(index-1):
                    curr = curr.next
                curr.next = curr.next.next
            self.size -=1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)