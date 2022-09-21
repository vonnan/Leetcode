class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic = {i: num for i, num in enumerate(nums)}
        
        tot = sum(num for i, num in enumerate(nums) if num % 2== 0)
        
        res = []
        
        for num, idx in queries:
            if dic[idx] % 2:
                dic[idx] += num
                if num % 2:
                    tot += dic[idx]
            else:
                
                if num % 2:
                    tot -= dic[idx]
                    
                else:
                    tot += num
                
                dic[idx] += num
            
            res.append(tot)
        
        return res
                
                    
                    