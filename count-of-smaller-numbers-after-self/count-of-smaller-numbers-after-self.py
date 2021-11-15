from bisect import bisect_left
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sort_, res = [], []
        for num in nums[::-1]:
            idx = bisect_left(sort_, num)
            res.append(idx)
            sort_.insert(idx, num)
        return res[::-1]