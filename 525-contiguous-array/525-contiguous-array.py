class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        ct = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                ct += 1
            else:
                ct -= 1
            
            if ct in dic:
                res = max(res, i - dic[ct])
            else:
                dic[ct] = i
        print(dic)    
        return res
        
        
                