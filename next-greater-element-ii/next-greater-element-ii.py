class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        max_num, n, stack = max(nums), len(nums), []
        nums += nums
        res = [-1] *2 * n
        
        for i in range(2 * n -1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
            
        return res[:n]