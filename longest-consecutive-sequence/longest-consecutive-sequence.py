class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = 0
        sets = set(nums)
        for num in sets:
            if num - 1 not in sets:
                nxt = num + 1
                while nxt in sets:
                    nxt += 1
                res = max(res, nxt - num)
        return res