class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front, back = [1], [1]
        
        for num in nums:
            front.append(front[-1] * num)
            
        for num in nums[::-1]:
            back.append(back[-1] * num)
        
        
        n = len(nums)
        
        dp = [1] * n
        
        for i in range(n):
            dp[i] = front[i] * back[n-1-i]
        
        return dp