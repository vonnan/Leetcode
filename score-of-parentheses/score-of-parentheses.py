from collections import deque
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for p in s:
            if p =="(":
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(last*2, 1)
        return stack[-1]