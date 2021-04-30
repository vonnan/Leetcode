class Solution:
    def knightDialer(self, n: int) -> int:
        move = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        mod = 10**9 + 7
        
        if n == 1:
            return 10
        
        ct = [1] * 10
        
        for _ in range(n-1):
            next_ct =[0]* 10
            for i in range(10):
                next_ct[i] = sum(ct[j] for j in move[i]) % mod
            ct = next_ct
        
        return sum(ct) % mod
            