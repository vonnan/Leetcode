class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        res = []
        
        if stamp[0] != target[0] or stamp[-1] != target[-1]:
            return res
        
        n = len(stamp)
        stamp, target = list(stamp), list(target)
        
        def check(i):
            changed = False
            for j in range(n):
                if target[i + j] == "?":
                    continue
                if target[i + j] != stamp[j]:
                    return False
                changed = True
            if changed:
                target[i: i + n] = ["?"] * n
                res.append(i)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(len(target) - n + 1):
                changed |= check(i)
                if target == ["?"] * len(target):
                    return res[::-1]
        return res[::-1] if target == ["?"] * len(target) else []
        
        
        
        