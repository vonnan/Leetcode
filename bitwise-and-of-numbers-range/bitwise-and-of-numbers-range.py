class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = bin(left)[2:], bin(right)[2:]
        print(left, right)
        if len(left) != len(right):
            return 0
        res, n = 0, len(left)
        for i in range(n):
            if left[i] == right[i] == "1":
                res = 2 * res + 1
            elif left[i] == right[i] == "0":
                res *= 2
            else:
                return res * 2 ** (n -i )
        return res
        
                