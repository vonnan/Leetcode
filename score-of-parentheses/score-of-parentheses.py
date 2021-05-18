from collections import deque
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, curr = [], 0
        for x in s:
            if x == "(":
                stack.append(curr)
                curr = 0
            else:
                curr += stack.pop() + max(curr, 1)
        return curr