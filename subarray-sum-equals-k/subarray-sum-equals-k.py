class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
            
        dic = defaultdict(list)
        res = 0
        for i, num in enumerate(presum):
            if num - k in dic:
                res += len(dic[num - k])
            dic[num].append(i)
        return res
    