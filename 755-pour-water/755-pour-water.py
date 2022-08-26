
class Solution:
    def pourWater(self, A: List[int], volume: int, k: int) -> List[int]:
        
        for _ in range(volume):
            idx = k
            for i in range(k-1, -1, -1):
                if A[i] > A[i + 1]:
                    break
                elif A[i] < A[i+1]:
                    idx = i
                    
                
            if idx != k:
                A[idx] += 1
                continue
                
            for j in range(k, len(A) - 1):
                if A[j] > A[j + 1]:
                    idx = j + 1
                elif A[j] < A[j + 1]:
                    break
            
            A[idx] += 1
            
        return A
                
                
                    
                
                
                
