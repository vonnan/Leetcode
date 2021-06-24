class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res =[]
        n, m = len(firstList), len(secondList)
        
        while i < n and j < m:
            l1,r1 = firstList[i]
            l2,r2 = secondList[j]
            left, right = max(l1, l2), min(r1, r2)
            
            if l1> r2:
                j += 1
                
            elif l2 > r1:
                i += 1
                
            else:
                res.append((left, right))
                if i+1 < n and r2 >= firstList[i+1][0]:
                    i += 1
                elif j +1 < m and r1 >= secondList[j+1][0]:
                    j += 1
                else:
                    i += 1
                    j += 1
                
        return res
    