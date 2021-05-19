class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left, right = 0, 0
        stack = []
        for val in s:
            stack.append(val)
            if val == "(":
                left+= 1
            elif val == ")":
                right+= 1
                
                if right > left:
                    stack.pop()
                    right -= 1
        if left == right:
            return "".join(stack)
        left, right = 0, 0
        
        stack_r = []
        for val in stack[::-1]:
            stack_r.append(val)
            if val == ")":
                right += 1
            elif val == "(":
                left += 1
                if left > right:
                    stack_r.pop()
                    left -= 1
        return "".join(stack_r[::-1])
            
            