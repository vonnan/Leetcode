from heapq import heappush
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0]
        for i, num in enumerate( nums + [0]):
            presum.append(num + presum[-1])
        res, mod = 0, 10**9 + 7
        
        left = []
        
        # left is to store the left (num, i)
        
        for i, num in enumerate(nums+[0]):
            start = i
            while left and left[-1][0] >= num:
                big, start = left.pop()
                res = max(res, (presum[i]- presum[start])* big)
            left.append((num, start))
            
        return res % mod
            
        
                    
                    
                
            