class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, res = 1, 0
        
        while i < n+1:
            if i not in nums:
                while sum(num for num in nums if num < i) >= i and i < n + 1:
                    i = sum(num for num in nums if num < i) + 1
                if i < n + 1 and i not in nums:
                    nums.append(i)
                    res += 1
            i += 1
        return res