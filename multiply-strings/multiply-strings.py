class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def chengfa(num, d):
            ans = 0
            for x in num:
                ans = ans * 10 + (ord(x) - ord("0")) * (ord(d) - ord("0"))
            return ans
        
        ans = 0
        
        for x in num2:
            ans = 10 * ans + chengfa(num1, x)
        
        return str(ans)
