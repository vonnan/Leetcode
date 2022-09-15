class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = Counter([])
        ct = 0
        
        left, res = 0, 0
        
        for right, c in enumerate(s):
            if c not in counter:
                ct += 1
            
            counter[c] += 1
            
            while ct > 2:
                counter[s[left]] -= 1
                if counter[s[left]] ==0:
                    counter.pop(s[left])
                    ct -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
                