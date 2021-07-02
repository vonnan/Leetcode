class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = Counter()
        left, ct, res, n = 0, 0, -inf, len(s)
        seen = set()
        
        for right, ch in enumerate(s):
            if ch not in seen:
                ct += 1
                seen.add(ch)
            
            counter[ch] += 1
            
            while ct > 2:
                if counter[s[left]] ==1:
                    
                    seen.remove(s[left])
                    ct -= 1
                counter[s[left]] -= 1
                left += 1
            
            print(right, counter, ct, left)
            res = max(res, right - left + 1)
            
        return res
            