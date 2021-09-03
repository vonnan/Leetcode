from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = [ord(ch) - ord("a") for ch in s1]
        s2 = [ord(ch) - ord("a") for ch in s2]
      
        target, window = [0] * 26, [0]* 26
        for ch in s1:
            target[ch] += 1
        
        for i, ch in enumerate(s2):
            window[ch] += 1
            if i >= len(s1):
                window[s2[i-len(s1)]] -= 1
            if window == target:
                return True
            
        return False
        
        
        