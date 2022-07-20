class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                else:
                    if stack:
                        stack.pop()
            return "".join(stack)
        
        return helper(s) == helper(t)