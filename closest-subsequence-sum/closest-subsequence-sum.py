class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        st1 = {0}
        st2 = {0}
        for i in range(n // 2):
            st1 |= {x + nums[i] for x in st1}
        for i in range(n // 2, n):
            st2 |= {x + nums[i] for x in st2}
        st1, st2 = sorted(st1), sorted(st2)
        n1, n2 = len(st1), len(st2)
        i, j = 0, n2 - 1
        res = abs(goal)
        while i <= n1 - 1 and j >= 0:
            if st1[i] + st2[j] - goal > 0:
                res = min(res, st1[i] + st2[j] - goal)
                j -= 1
            elif st1[i] + st2[j] - goal < 0:
                res = min(res, goal - st1[i] - st2[j])
                i += 1
            else:
                return 0
        return res