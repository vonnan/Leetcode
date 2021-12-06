class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = deque(num)
        if k == len(num):
            return "0"
        
        stack = []
        
        for c in num:
            while stack and stack[-1] > c and k:
                stack.pop()
                k -= 1
            stack.append(c)
        
        while k:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == "0":
            stack.pop(0)
            
        return "".join(stack) if stack else "0"
        
                    