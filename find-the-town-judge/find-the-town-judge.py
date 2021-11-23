class Solution:
    def findJudge(self, n: int, A: List[List[int]]) -> int:
        sets1 = set(range(1, n+1)) - set(i for i,_ in A)
        if not sets1:
            return -1
        
        for i in sets1:
            if len(set(j for j, k in A if k ==i))== n-1:
                return i
        return -1