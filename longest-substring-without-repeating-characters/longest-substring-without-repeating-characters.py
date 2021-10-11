class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res, counter  = 0, 0, Counter()
        
        for right, c in enumerate(s):
            counter[c] += 1
            while counter[c] > 1:
                counter[s[left]] -= 1
                if not counter[s[left]]:
                    del counter[s[left]]
                left += 1
            res = max(res, right -left + 1)
                
        return res