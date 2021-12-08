class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum = [0]
        stack = []
        res = inf
        
        for num in nums:
            presum.append(num + presum[-1])
            
        for i, p in enumerate(presum):
            while stack and presum[stack[-1]] >= p:
                stack.pop()
                
            while stack and p - presum[stack[0]] >= k:
                res = min(res, i - stack.pop(0))
            
            stack.append(i)
        
        return res if res != inf else -1