class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        left, count, res =0, 0, 0
        seen = set([])
        
        for right, ch in enumerate(s):
            if ch not in seen:
                count += 1
                seen.add(ch)
                
            counter[ch] += 1
            
            while count > k:
                if counter[s[left]] == 1:
                    count -= 1
                    seen.remove(s[left])
                    del counter[s[left]]
                else:
                    counter[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
                