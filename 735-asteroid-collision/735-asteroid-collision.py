class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        n = len(A)
        
        stack = [A[0]]
        for a in A[1:]:
            if not stack or stack[-1] * a > 0 or (stack[-1] < 0 and a > 0):
                stack.append(a)
            else:
                flag = True
                while stack and stack[-1] > 0:
                    if stack[-1] + a == 0:
                        stack.pop()
                        flag = False
                        break
                    elif stack[-1] + a > 0:
                        flag = False
                        break
                    else:
                        stack.pop()
                if flag:
                    stack.append(a)
        
        return stack
                        
                    
        
                
            
            