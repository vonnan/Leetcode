class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter = Counter()
        n = len(text)
        j, res = 0, 1
        ct = Counter(text)
        for i, ch in enumerate(text):
            counter[ch] += 1
            while j < i and len(counter) >2 or (len(counter)==2 and min(counter.values()) >1):
                counter[text[j]] -= 1
                if counter[text[j]] == 0:
                    del counter[text[j]]
                j += 1
            if len(counter) == 1:
                res = max(res, i - j + 1)
            else:
                if i - j + 1 == 2:
                    if ct[ch] > 1 or ct[text[i-1]] >1:
                        res = max(res, 2)
                else:
                    for key, val in counter.items():
                        if val > 1:
                            if ct[key] == val:
                                res = max(res, val)
                            else:
                                res = max(res, val + 1)
                    
            
        
        return res
            
                
                