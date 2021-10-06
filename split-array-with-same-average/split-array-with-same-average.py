class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        tot, avg = sum(nums), sum(nums)/n
        lst = [k for k in range(1, (n +1)//2 + 1) if tot * k %n == 0]

        if not lst or n == 1:
            return False
        
        
        memo = defaultdict(set)
        memo[0] = {0}
        
        for num in nums:
            for size in range((n+1)//2, 0, -1):
                target = tot * size 
                for prev in memo[size -1]:
                    memo[size].add(prev + num)
                    if (prev + num)* n == target:
                        print(num, size, avg, target/n)
                        return True
        return False
                    
        
            
        
        
    
        
                   