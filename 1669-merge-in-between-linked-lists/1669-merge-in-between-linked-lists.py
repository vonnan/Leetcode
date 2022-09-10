# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        level = 0
        node = list1
        while node:
            node = node.next
            level += 1
            if level == b + 1:
                break
        
        dummy = ListNode(-1)
        dummy.next = list1
        node1 = dummy
        
        level = 0
        while node1:
            if level == a:
                break
            node1 = node1.next
            level += 1
        
        node1.next = list2
        
        while node1:
            if node1.next:
                node1 = node1.next
            else:
                node1.next = node
                break
        return dummy.next
            
        
        
            
        
            