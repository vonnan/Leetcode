class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while "**" in p:
            p = p.replace("**", "*")
        
        dp = {}
        
        def helper(s, p):
            if (s,p) not in dp:
                
                if s== p or p == "*":
                    dp[(s,p)] = True
                elif s == "" or p == "":
                    dp[(s,p)] = False
                elif s[0] == p[0] or p[0] == "?":
                    dp[(s,p)] = helper(s[1:], p[1:])
                elif p[0] == "*":
                    dp[(s,p)] = helper(s, p[1:]) or helper(s[1:], p)
                else:
                    dp[(s,p)] = False
            
            return dp[(s,p)]
        
        return helper(s, p)
                