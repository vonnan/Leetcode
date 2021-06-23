class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        ref = 0
        
        for i in range(1, n+1):
            ref ^= i
            
        # ref = 1 ^ 2 ^ 3 ^... ^ n
        
        for j in range(1, n, 2):
            ref ^= encoded[j]
            
        res = [ref]
        #ref: perm[0]
        
        for i in range(n-1):
            res.append(res[-1]^encoded[i])
        
        return res
            
            
        
        
            
            