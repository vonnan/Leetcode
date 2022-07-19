class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        
        ct = Counter()
        
        res, n, stack  = [], len(p), []
        
        for i, c in enumerate(s):
            if c not in counter:
                ct = Counter()
                stack = []
            else:
                ct[c] += 1
                stack.append(c)
            
                while ct[c] > counter[c]:
                    ct[stack.pop(0)] -= 1
                if ct == counter:
                    res.append(i - n + 1)
                
                        
        return res
                    
                    
                
            