class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        
        for c in s:
            if c != ")":
                stack.append(c)
            else:
                tmp = ""
                while stack[-1] != "(":
                    tmp = stack.pop() + tmp
                stack.pop()
                
                tmp = tmp.replace("--", "+")
                tmp = tmp.replace("-", "+-")
                stack.append(str(sum(int(x) for x in tmp.split("+") if x)))
        ans = "".join(stack)
        
        ans = ans.replace("--", "+")
        ans = ans.replace("-", "+-")
        
        return sum(int(x) for x in ans.split("+") if x)
            