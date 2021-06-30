# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.listNode = head
        self.length = 0
        self.temp, temp = head, head
        while temp.next:
            self.length += 1
            temp = temp.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        val= random.randint(0, self.length)
        temp = self.temp
        while val:
            temp = temp.next
            val -= 1
        return temp.val
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()