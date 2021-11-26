class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = [0]
        res = 0
        dic = defaultdict(int)
        dic[0] = -1
        
        for i, num in enumerate(nums):
            nxt = presum[-1] + num
            if nxt - k in dic:
                res = max(res, i - dic[nxt - k])
            if nxt not in dic:
                dic[nxt] = i
            presum.append(nxt)
        
        return res