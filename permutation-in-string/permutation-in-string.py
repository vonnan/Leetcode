class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = [ord(ch) - ord("a") for ch in s1]
        s2 = [ord(ch) - ord("a") for ch in s2]
        
        target, window =[0] * 26, [0] * 26
        n = len(s1)
        for ch in s1:
            target[ch] += 1
        
        for i, ch in enumerate(s2):
            window[ch] += 1
            if i >= n:
                window[s2[i - n]]-= 1
            if target == window:
                return True
        return False
    
        
        