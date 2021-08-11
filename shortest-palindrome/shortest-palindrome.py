class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        flag = False
        for i in range(len(s)//2, 0, -1):
            if s[:i] == s[i+1:2*i + 1][::-1] or s[:i] == s[i:2*i][::-1]:
                flag = True
                break
        
        if not flag:
            return s[1:][::-1] + s
        if s[:i] == s[i+1:2*i + 1][::-1]:
            return s[-(len(s) - (2*i + 1)):][::-1] + s
        
        else:
            return s[-(len(s) - 2*i):][::-1] + s
            
            