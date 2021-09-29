class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        n = len(s)
        counter = Counter()
        
        for right, c in enumerate(s):
            while c in counter:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            counter[c] = 1
            res = max(res, right - left + 1)
        
        return res