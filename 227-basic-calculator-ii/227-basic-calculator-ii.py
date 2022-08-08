class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        s = s.replace("-", "+-").replace(" ", "")
        s = s.split("+")
        print(s)
        def helper(s):
            sign, d, stack, func  = "", "", [], []
            if s[0] == "-":
                sign = "-"
                s = s[1:]
                
            for c in s:
                if c.isdigit():
                    d += c
                else:
                    stack.append(int(d))
                    d = ""
                    func.append(c)
            stack.append(int(d))
            if not func:
                return stack[0] if not sign else (-1) * stack[0]
            
            first = stack.pop(0)
            for c in func:
                second = stack.pop(0)
                
                if c == "*":
                    first *= second
                else:
                    first //= second
            return first if not sign else (-1) * first 
        
        return sum(helper(oper) for oper in s if oper)
                    
                    