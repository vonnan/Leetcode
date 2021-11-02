class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1, num2 = list(num1), list(num2)
        num1 = list(map(int, num1))
        num2 = list(map(int, num2))
        print(num1, num2)
        n1, n2 = len(num1), len(num2)
        
        res = []
        max_=0
        for i in range(n1-1, -1, -1):
            carry = 0
            tmp = [0]*(n1-1-i) + []
            ni = num1[i]
            for j in range(n2-1, -1, -1):
                carry, r  = divmod(ni * num2[j] + carry, 10)
                tmp.append(r)
            if carry:
                tmp.append(carry)
            max_= max(max_, len(tmp))
            res.append(tmp)
            
        carry = 0
        n = len(res)
        ans = ""
        for _ in range(max_):
            tmp = 0
            for i in range(n):
                if res[i]:
                    tmp += res[i].pop(0)
            tmp += carry
            carry, r = divmod(tmp, 10)
            ans += str(r)
        
        ans =  ans[::-1]
        
        if carry:
            ans = str(carry) + ans
        
        return ans 
            
                
        