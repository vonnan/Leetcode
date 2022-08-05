class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, counter, res = 0, Counter([]), 0
        
        for right, c in enumerate(s):
            counter[c] += 1
            while counter[c] > 1:
                counter[s[left]] -= 1
                left += 1
            res = max(right - left + 1, res)
        
        return res
            