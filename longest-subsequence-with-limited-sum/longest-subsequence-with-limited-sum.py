class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        presum = [0] + list(accumulate(nums))
        res = []
        for target in queries:
            left, right = 0, len(nums)
            if target >= presum[right]:
                res.append(right)
                continue
            
            while left < right:
                mid = (left + right + 1)//2
                
                if presum[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            
            res.append(left)
        
        return res
                    