class Solution:
    def findMinMoves(self, A: List[int]) -> int:
        n = len(A)
        if sum(A) % n:
            return -1
        
        target = sum(A)//n
        A = [num - target for num in A]
        res = max(A)
        
        to_right = 0
        for num in A:
            to_right += num
            res = max(res, abs(to_right))
        return res
            
        
        