class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = data.count(1)
        n = len(data)
        ct = data[:ones].count(0)
        res = ct
        for i in range(ones, n):
            ct += (data[i] == 0) - (data[i-ones] == 0)
            res = min(res, ct)
        return res