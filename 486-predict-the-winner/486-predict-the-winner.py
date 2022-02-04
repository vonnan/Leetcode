class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs(left, right):
            if (left, right) not in memo:
                if left > right:
                    memo[(left, right)] = 0
                
                elif left == right:
                    memo[(left, right)] = nums[left]
                else:    
                    pick_left = nums[left] + min(dfs(left + 2, right), dfs(left + 1, right -1))
                    pick_right = nums[right] + min(dfs(left + 1, right -1), dfs(left, right -2))
                
                    memo[(left, right)] = max(pick_left, pick_right)
                
            return memo[(left, right)]
        
        return dfs(0, len(nums) -1) >= (sum(nums)/2)
                
                