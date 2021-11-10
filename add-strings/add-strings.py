class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry = "", 0
        num1, num2 = list(num1), list(num2)
        while num1 and num2:
            n1, n2 = int(num1.pop()), int(num2.pop())
            carry, n = divmod(n1 + n2 + carry, 10)
            res = str(n) + res
        
        num = (num1 or num2)
        
        while num:
            carry, n = divmod(int(num.pop()) + carry, 10)
            res = str(n) + res
            
        if carry:
            res = str(carry) + res
        
        return res