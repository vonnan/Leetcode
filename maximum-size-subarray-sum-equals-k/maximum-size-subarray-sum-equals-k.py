class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        dic = {}
        res = 0
        for i, num in enumerate(presum):
            if num - k in dic:
                res = max(res, i - dic[num - k])
            if num not in dic:
                dic[num] = i
        return res
                
            