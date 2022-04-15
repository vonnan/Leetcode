class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        
        for c in s:
            if c != ")":
                stack.append(c)
            else:
                res = []
                while stack[-1] != "(":
                    res.append(stack.pop())
                    
                stack.pop()
                stack.extend(res)
                
                
        return "".join(stack)
                    
                    