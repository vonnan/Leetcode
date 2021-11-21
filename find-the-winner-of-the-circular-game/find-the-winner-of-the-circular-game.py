from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        
        stack = list(range(1, n + 1))
        
        while stack:
            i = 1
            while i < k:
                stack.append(stack.pop(0))
                i += 1
            stack.pop(0)
            if len(stack) == 1:
                return stack[0]
