class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        presum, res = 0, 0
        for num in nums:
            presum += num
            if presum - k in dic:
                res += dic[presum - k]
            dic[presum] += 1
        return res
        