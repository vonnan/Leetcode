class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        
        dic = defaultdict(int)
        dic[0] = 1
        
        res = 0
        for i, num in enumerate(nums):
            last = presum[-1] + num
            presum.append(last)
            if last - k in dic:
                res += dic[last - k]
            dic[last] += 1
        return res