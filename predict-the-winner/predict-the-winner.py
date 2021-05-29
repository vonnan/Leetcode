class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            
            if left > right:
                return 0
            
            if left == right:
                return nums[left]
            
            pick_left = nums[left] + min(dfs(left+1, right -1), dfs(left + 2, right))
            pick_right = nums[right] + min(dfs(left+1, right-1), dfs(left, right -2))
            
            score = max(pick_left, pick_right)
            
            memo[(left, right)] = score
            
            return score
        
        score = dfs(0, len(nums) - 1)
        
        
        return 2 * score >= sum(nums)