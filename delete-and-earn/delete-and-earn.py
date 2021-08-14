class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        lst = [num for num in sorted(counter)]
        prepre, pre, pre_num = 0, 0, -inf
        for num in lst:
            if num > pre_num + 1:
                curr = pre + counter[num] * num 
            else:
                curr = max(prepre + counter[num] * num, pre)
            
            prepre, pre, pre_num = pre, curr, num
            
        return curr
        
            
            
                
                