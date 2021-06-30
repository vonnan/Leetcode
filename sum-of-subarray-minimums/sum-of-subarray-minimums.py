class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n, mod = len(arr), 10**9 + 7
        left, right = [1] * n, [1] * n
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - i
            stack.append(i)
            
        stack = []
        
        for j in range(n):
            while stack and arr[stack[-1]] > arr[j]:
                stack.pop()
            if stack:
                left[j] = j - stack[-1]
            else:
                left[j] = j + 1
            stack.append(j)
        print(left, right)    
        return sum(left[i]* right[i]*arr[i] for i in range(n))%mod
            
                
        
            
        