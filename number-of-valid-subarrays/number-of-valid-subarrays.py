class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        n = len( nums)
        stack = [[-inf, n]]
        res = 0
        for i in range(n-1, -1, -1):
            while stack[-1][0] >= nums[i]:
                stack.pop()
            res += stack[-1][1] - i
            stack.append((nums[i], i))
        return res
            