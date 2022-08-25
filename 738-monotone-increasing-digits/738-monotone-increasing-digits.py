class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        res = ""
        prev = 0
        if n < 10:
            return n
        
        s = str(n)
        n = len(s)
        for i in range(1, n + 1):
            if i == n:
                while prev < i:
                    res += s[prev]
                    prev += 1
            elif s[prev] == s[i]:
                continue
            elif s[prev] < s[i]:
                while prev < i:
                    res += s[prev]
                    prev += 1
            else:
                res += str(int(s[prev]) - 1)
                res += "9" * (n - len(res))
                return int(res)
        return int(res)
                
            
        