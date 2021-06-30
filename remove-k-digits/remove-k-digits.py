class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = deque(num)
        stack = []
        
        while q:
            while stack and stack[-1] > q[0] and k:
                stack.pop()
                k -= 1
                if k== 0:
                    stack.extend(q)
                    return str(int("".join(stack)))
            stack.append(q.popleft())
        if k:
            stack = stack[:-k]
            
        return str(int("".join(stack))) if stack else "0"
            
        
        