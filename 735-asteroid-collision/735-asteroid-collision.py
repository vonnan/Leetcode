class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        stack = []
        for a in A:
            flag = True
            if a < 0:
                while stack and stack[-1] > 0:
                    if a + stack[-1] == 0:
                        stack.pop()
                        flag = False
                        break
                    elif a + stack[-1] > 0:
                        flag = False
                        break
                    else:
                        stack.pop()
            if flag: 
                stack.append(a)
            
        return stack
            
                        
                       
                    
                    
        
