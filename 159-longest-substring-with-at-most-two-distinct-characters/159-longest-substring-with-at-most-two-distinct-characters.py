class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = Counter()
        ct = 0
        
        left, res = 0, 0
        for right, c in enumerate(s):
            if c not in counter:
                ct += 1
                
            
            while ct > 2:
                
                if counter[s[left]]== 1:
                    ct -= 1
                    counter.pop(s[left])
                else:
                    counter[s[left]] -= 1
                left += 1
                
                         
            counter[c] += 1
            
            res = max(res, right - left + 1)
                
        return res
            