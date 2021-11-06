class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        ct = 0
        left, res = 0, 0
        counter = Counter()
        
        for right, c in enumerate(s):
            if c not in counter:
                ct += 1
                while ct == k + 1:
                    if counter[s[left]] == 1:
                        ct -= 1
                        counter.pop(s[left])
                    else:
                        counter[s[left]] -= 1
                    left += 1
            
            counter[c] += 1
            res = max(res, right - left + 1)
        return res