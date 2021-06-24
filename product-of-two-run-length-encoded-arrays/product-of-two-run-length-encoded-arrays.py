class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        m, n = len(encoded1), len(encoded2)
        
        while i < m and j < n:
            num1, f1 = encoded1[i]
            num2, f2 = encoded2[j]
            res.append([num1 * num2, min(f1, f2)])
            if f1 < f2:
                i += 1
                encoded2[j][1] -= f1
            elif f2 < f1:
                j += 1
                encoded1[i][1] -= f2
            else:
                i += 1
                j += 1
        
        ans = []
        while res:
            num, f = res.pop()
            
            while res and res[-1][0]== num:
                f += res.pop()[1]
                
            ans.append((num, f))
            
            
        return ans[::-1]
            