class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        flips = 0
        
        if not A[0]:
            for i in range(K):
                A[i] = 1 - A[i]
            flips += 1
        
        diffs = [abs(A[i+1] - A[i]) for i in range(N-1)]
        for i in range(N-K):
            if diffs[i]:
                flips += 1
                if i < N - K - 1:
                    diffs[i+K] = 1 - diffs[i+K]
                
        return flips if not any(diffs[N-K:]) else -1