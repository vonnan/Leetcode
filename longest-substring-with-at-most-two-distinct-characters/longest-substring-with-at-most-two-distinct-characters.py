from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = Counter()
        res = i = 0
        seen = set()
        count = 0
        for j, ss in enumerate(s):
            if ss not in seen:
                count += 1
                seen.add(ss)
            counter[ss] += 1
            
            while count > 2:
                if counter[s[i]] ==1:
                    count -= 1
                    seen.remove(s[i])
                counter[s[i]] -= 1
                i += 1
            
            res = max(res, j-i+1)
            
        return res
            
            
            
            
        
        