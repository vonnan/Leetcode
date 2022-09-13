class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        res = set()
    
        for i in range(len(s)):
            dict1 = defaultdict(int)
            j = i + 1
            for c in s[i:]:
                dict1[c] += 1
            
                if len(set(dict1.values())) == 1:
                    res.add(s[i:j])
                
                j += 1
            
        return len(res)                
        
        
        
        
            