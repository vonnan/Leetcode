class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def helper(x):
            res, diff = 0, 1
            while x <= n:
                res += min(n - x + 1, diff)
                x *= 10
                diff *= 10
            return res
        
        res = 1
        while k > 1:
            ct = helper(res)
            print(k, ct, res)
            if k > ct:
                res += 1
                k -= ct
            else:
                res *= 10
                k -= 1
            print("after", k, ct, res)
            
        
        return res
                
            