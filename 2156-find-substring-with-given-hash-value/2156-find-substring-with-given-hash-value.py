class Solution:
    def subStrHash(self, s: str, p: int, mod: int, k: int, hashValue: int) -> str:
        a, n = ord("a"), len(s)
        x = [ord(c) - a + 1  for c in s]
        pk, curr= pow(p, k, mod), 0
        for i in range(n-1, -1, -1):
            curr = (curr * p + x[i])%mod
            if i + k < n:
                curr=(curr -x[i+k] * pk)%mod   
            if curr == hashValue:
                idx = i
        return s[idx:idx + k]
        
        