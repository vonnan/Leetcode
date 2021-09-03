class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        counter = Counter()
        
        for right, ch in enumerate(s):
            counter[ch] += 1
            while counter[ch] > 1:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res