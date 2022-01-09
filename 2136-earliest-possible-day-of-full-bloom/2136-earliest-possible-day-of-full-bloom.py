class Solution:
    def earliestFullBloom(self, PT: List[int], GT: List[int]) -> int:
        pairs = [(g,p) for g, p in zip(GT, PT)]
        pairs.sort()
        
        GT, PT = [g for g, _ in pairs], [p for _,p in pairs]
        
        prefix = [0]
        for p in PT:
            prefix.append(prefix[-1]+ p)
        
        tot = prefix[-1]
        res = prefix[-1]
        for i, g in enumerate(GT):
            res = max(res, tot - prefix[i] + g)
            
        return res