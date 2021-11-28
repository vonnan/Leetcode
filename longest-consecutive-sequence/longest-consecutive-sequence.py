class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        res = 0
        for num in sets:
            if num -1 not in sets:
                nxt = num +1
                while nxt in sets:
                    nxt += 1
                res = max(res, nxt - num)
        return res
            