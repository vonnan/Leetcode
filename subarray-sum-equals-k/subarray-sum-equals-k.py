class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        dic, res = {}, 0
        for key in presum:
            if key - k in dic:
                res += dic[key - k]
                
            if key not in dic:
                dic[key] = 1
            else:
                dic[key] += 1
                
        return res