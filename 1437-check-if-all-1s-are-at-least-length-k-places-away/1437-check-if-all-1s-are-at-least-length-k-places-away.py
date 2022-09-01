class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lst = [i for i, num in enumerate(nums) if num]
        for a, b in zip(lst, lst[1:]):
            if b - a <= k:
                return False
        return True