class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        
        ref = 0
        for i in range(1, n+1):
            ref ^= i
            
        for j in range(1, n, 2):
            ref ^= encoded[j]
        
        res = []
        res.append(ref)
        
        for e in encoded:
            res.append(res[-1] ^ e)
            
        return res