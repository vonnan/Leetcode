class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {1: 1, 2:2}
        for i in range(n + 1):
            if i > 2:
                dic[i] = dic[i-1] + dic[i - 2]
        return dic[n]