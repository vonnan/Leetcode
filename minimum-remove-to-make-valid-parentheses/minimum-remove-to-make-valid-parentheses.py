class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        sets = set()
        for i, c in enumerate(s):
            if c in "()":
                if c == "(":
                    stack.append(i)
                else:
                    if not stack:
                        sets.add(i)
                    else:
                        stack.pop()
        sets |= set(stack)
        res = ""
        for i, c in enumerate(s):
            if i in sets:
                continue
            res += c
        
        return res
                    