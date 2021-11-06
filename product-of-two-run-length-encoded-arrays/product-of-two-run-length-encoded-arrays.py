class Solution:
    def findRLEArray(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            num1, f1 = A[i]
            num2, f2 = B[j]
            f = min(f1, f2)
            if res and res[-1][0] == num1 * num2:
                res[-1][1] += f
            else:
                res.append([num1 * num2, f])
            
            if f1 < f2:
                i += 1
                B[j][1] -= f1
            
            elif f1 > f2:
                j += 1
                A[i][1] -= f2
            
            else:
                i += 1
                j += 1
                
        return res
                
