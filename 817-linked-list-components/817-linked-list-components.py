# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        nums = set(nums)
        
        res = 0
        flag = False
        while head:
            val = head.val
            if val not in nums:
                if flag:
                    res += 1
                flag = False
                
            else:
                flag = True
                nums.remove(val)
                if not nums:
                    return res + 1
            head = head.next
            
                
                
                