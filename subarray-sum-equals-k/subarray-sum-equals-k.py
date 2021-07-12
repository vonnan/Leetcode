class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        dic = defaultdict(int)
        res = 0
        for i, num in enumerate(presum):
            if num - k in dic:
                res += dic[num - k]
            dic[num] += 1
            
        return res
            