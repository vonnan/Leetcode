class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        while matrix:
            res.extend(matrix.pop(0))
            if not matrix:
                return res
            
            for r in range(len(matrix)):
                if matrix[r]:
                    res.append(matrix[r].pop())
            
            if not matrix:
                return res
            
            res.extend(matrix.pop()[::-1])
            
            if not matrix:
                return res
            
            for r in range(len(matrix)-1, -1, -1):
                if matrix[r]:
                    res.append(matrix[r].pop(0))
                
            if not matrix:
                return res
        return res
                
            
            
            
            
            
            