class Solution:
    def findJudge(self, n: int, A: List[List[int]]) -> int:
        trusted ={i:0 for i in range(1,n+1)}
        trust ={i:0 for i in range(1,n+1)}
        sets = set()
        for a,b in A:
            trusted[b] += 1
            trust[a] += 1
        for i in range(1,n+1):
            if trusted[i] == n-1 and trust[i] ==0:
                return i
        return -1