class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        
        res = []
        
        while i < m and j < n:
            l1, r1 = firstList[i]
            l2, r2 = secondList[j]
            
            if r1< l2:
                i += 1
            
            elif r2 < l1:
                j += 1
                
            else:
                l = max(l1, l2)
                if r1 < r2:
                    i += 1
                    res.append((l, r1))
                else:
                    j += 1
                    res.append((l, r2))
                    
        return res
            
                