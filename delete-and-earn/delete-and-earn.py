class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        prepre, pre, prenum = 0, 0, -inf
        nums.sort()
        counter = Counter(nums)
        
        for num in sorted(counter.keys()):
            if num > prenum + 1:
                curr = pre + counter[num] * num
                
            else:
                curr = max(pre, prepre + counter[num] * num)
                
            prepre, pre, prenum = pre, curr, num
            
        return curr