class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c not in "+-*/":
                stack.append(c)
            else:
                a, b = int(stack.pop()), int(stack.pop())
                if c == "+":
                    stack.append(a+b)
                elif c == "-":
                    stack.append(b - a)
                elif c == "*":
                    stack.append(a * b)
                else:
                    stack.append(b / a)
        
        return int(stack[0])