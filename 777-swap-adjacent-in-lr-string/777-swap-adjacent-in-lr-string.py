class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = [i if c == "L" else -i for i, c in enumerate(start, 1) if c in "LR"]
        e = [i if c == "L" else -i for i, c in enumerate(end, 1) if c in "LR"]
        
        return len(s) == len(e) and start.count("L") == end.count("L") and all(a >= b for a,b in zip(s,e))
