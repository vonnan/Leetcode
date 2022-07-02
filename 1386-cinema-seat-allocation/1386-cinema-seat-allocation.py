class Solution:
    def maxNumberOfFamilies(self, n: int, A: List[List[int]]) -> int:
        A.sort(reverse = 1)
        A = [(u, v) for u, v in A if v not in set([1,10])]
        print(A)
        if not A:
            return n * 2
        
        
        def tot(sets):
            if len(sets) > 4:
                return 0
            if 2 not in sets and 3 not in sets and 4 not in sets and 5 not in sets:
                return 1
            if 4 not in sets and 5 not in sets and 6 not in sets and 7 not in sets:
                return 1
            if 6 not in sets and 7 not in sets and 8 not in sets and 9 not in sets:
                return 1
            return 0
        res, start = 0, 1   
        while A:
            
            row, col = A.pop()
            
            res += (row - start) * 2
            
            start = row + 1
            sets = set([col])
            while A and A[-1][0] == row:
                r, c = A.pop()
                sets.add(c)
            
            res += tot(sets)
            
            
        res += (n-row) * 2
        return res
        
        
            
            
            
                
            
                
                
                
            
        
        
            