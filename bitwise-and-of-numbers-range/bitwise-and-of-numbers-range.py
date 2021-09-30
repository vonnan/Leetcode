class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = bin(left)[2:], bin(right)[2:]
        
        if len(left) != len(right):
            return 0
        
        n, res = len(right), 0
        
        for i in range(n):
            if left[i] == right[i] == "1":
                res = 2*res + 1
            elif left[i] == right[i] == "0":
                res *= 2
            else:
                return res * 2**(n-i)
        return res