
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        stack, n = [], len(arr)
        next_high, next_low = [0]*n, [0]*n
        
        lst_high = sorted([(a,i) for i,a in enumerate(arr)])
        lst_low = sorted([(-a,i) for i, a in enumerate(arr)])
        print(lst_high)
        print(lst_low)
        
        for a, i in lst_high:
            while stack and stack[-1] < i:
                next_high[stack.pop()] = i
            stack.append(i)
        print(stack)
        print(next_high)
        stack = []    
        for a, i in lst_low:
            while stack and stack[-1] < i:
                next_low[stack.pop()] = i
            stack.append(i)
        print(stack)
        print(arr, next_high, next_low)
        
        high, low = [0]*n, [0]*n
        high[n-1] , low[n-1] = 1, 1
        for i in range(n-2, -1, -1):
            high[i] = low[next_high[i]]
            low[i] = high[next_low[i]]
            
        return sum(high)
    
        stack, n = [], len(arr)
        next_high, next_low =[0] * n, [0] * n
        
        lst_high = sorted([(a, i) for i, a in enumerate(arr)])
        lst_low = sorted([(-a, i) for i, a in enumerate(arr)])
        
        for a,i in lst_high:
            while stack and stack[-1] < i:
                next_high[stack.pop()] = i
            stack.append(i)
        
        for a, i in lst_low:
            while stack and stack[-1] < i:
                next_low[stack.pop()] = i
            stack.append(i)
            
        high, low = [0] * n, [0]* n
        for i in range(n-2, -1, -1):
            high[i] = low[next_high[i]]
            low[i] = high[next_low[i]]
            
        return sum(high)
            
        
            
                
        
            
            
        