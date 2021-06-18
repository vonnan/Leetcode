from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = [ord(c) - ord("a") for c in s1]
        s2 = [ord(c) - ord("a") for c in s2]
        
        target = [0] * 26
        for c in s1:
            target[c] += 1
            
        window = [0] * 26
        for i,c in enumerate(s2):
            window[c] += 1
            if i >= len(s1):
                window[s2[i-len(s1)]] -= 1
            if window == target:
                return True
        return False
        
        
        