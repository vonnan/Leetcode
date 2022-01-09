class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = "a", "b"
        
        if x < y:
            x, y = y, x
            a, b = b, a
        
        res = 0
        counter = Counter()
        
        for ch in s + "x":
            if ch in "ab":
                if ch == b and counter[a] > 0:
                    res += x
                    counter[a] -= 1
                else:
                    counter[ch] += 1
            
            else:
                res += y * min(counter[a], counter[b])
                counter = Counter()
        
        return res