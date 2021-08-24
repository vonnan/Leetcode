class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        #all
        ref = 1
        n = len(encoded) + 1
        for i in range(2, n+1):
            ref ^= i
        
        #ref= 1^2^3...^n
        
        for i in range(1, n, 2):
            ref ^= encoded[i]
        #ref: now is b0
        res =[ref]
        #print(ref, res)
        for j in range(0, n-1):
            print(j, encoded[j])
            res.append(res[-1] ^ encoded[j])
            
        return res
        