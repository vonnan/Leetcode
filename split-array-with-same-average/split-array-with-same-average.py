from collections import defaultdict
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n, tot = len(nums), sum(nums)
        if not any(k * tot %n ==0 for k in range(1, (n+1)//2+1)) or n <=1:
            return False
    
        
        memo= defaultdict(set)
        #total sum with the key of size
        
        memo[0] = {0}
        
        for num in nums:
            for size in range((n+1)//2, 0, -1):
                for prev in memo[size -1]:
                    memo[size].add(prev + num)
                    
                    if (prev + num)* n == tot * size:
                        return True
                
        return False
                
                
        
                
                
            
        
       