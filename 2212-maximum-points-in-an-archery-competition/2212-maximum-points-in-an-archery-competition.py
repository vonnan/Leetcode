class Solution:
    def maximumBobPoints(self, N: int, A: List[int]) -> List[int]:
        max_ = 0
        for i in range(1, 1<<12):
            lst, ct, score = [0] * 12, 0, 0
            flag = True
            for j in range(12):
                if (1<<j) & i:
                    lst[j] = A[j] + 1
                    ct += lst[j]
                    score += j
                    if ct > N:
                        flag = False
                        break
            if flag:
                if score > max_:
                    max_ = score
                    res = lst[:]
                    
                    
        extra = N - sum(res)   
        if extra:
            res[0] += extra
        return res
                
            