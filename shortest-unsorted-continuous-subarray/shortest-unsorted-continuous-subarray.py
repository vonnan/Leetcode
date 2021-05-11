class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_lst = sorted(nums)
        
        res = 0
        
        for i, num in enumerate(nums):
            if num == sort_lst[i]:
                res += 1
                
            else:
                break
        
        n = len(nums)
        if res == n:
            return 0
        
        for i in range(n-1, -1, -1):
            if nums[i] == sort_lst[i]:
                res += 1
            else:
                break
                
        return n - res
                
        