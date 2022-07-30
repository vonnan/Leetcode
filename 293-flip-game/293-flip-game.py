class Solution:
    def generatePossibleNextMoves(self, A: str) -> List[str]:
        if "++" not in A:
            return []
        
        res = []
        start = 0
        n = len(A)
        while start < n:
            if "++" not in A[start:]:
                return res
            
            idx = A.find("++", start)
            res.append(A[:idx] + "--" + A[idx+2:])
            start = idx + 1
            
        return res
            