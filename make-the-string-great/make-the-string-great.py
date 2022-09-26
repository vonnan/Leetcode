class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if (c != c.lower() and stack and stack[-1] == c.lower()) or (c != c.upper() and stack and stack[-1] == c.upper()):
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack) if stack else ""