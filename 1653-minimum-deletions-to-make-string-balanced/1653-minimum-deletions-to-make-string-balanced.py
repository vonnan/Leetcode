class Solution:
    def minimumDeletions(self, s: str) -> int:
        s = list(s)
        while s and s[-1] == "b":
            s.pop()
            
        while s and s[0] == "a":
            s.pop(0)
            
        prefix, suffix = [0], [0]
        for c in s:
            if c == "b":
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        
        for c in s[::-1]:
            if c == "a":
                suffix.append(suffix[-1] + 1)
            else:
                suffix.append(suffix[-1])
        
        suffix = (suffix[::-1])
        
        return min(a + b for a, b in zip(prefix, suffix))
        