class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        res = ""
        k -= 1
        while n:
            n -= 1
            pos, k = divmod(k, math.factorial(n))
            res += str(nums.pop(pos))
        return res
            
        