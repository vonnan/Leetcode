class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        res, carry = "", 0
        
        while num1 and num2:
            carry, num = divmod(int(num1.pop()) + int(num2.pop()) + carry, 10)
            res = str(num) + res
            
        if not num1 and not num2:
            if carry:
                res = str(carry) + res
        
        else:
            nums = num1 or num2
            while nums:
                carry, num = divmod(int(nums.pop()) + carry, 10)
                res = str(num) + res
            if carry:
                res = str(carry) + res
        
        return res