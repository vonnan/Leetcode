class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        counter = Counter([])
        res = 1
        for i, c in enumerate(s):
            pre = c
            counter[pre] += 1
            for j in range(i + 1, n):
                pre += s[j]
                counter[pre] += 1
                
        lst = [len(key) for key, val in counter.items() if val > 1]  
        return max(lst) if lst else 0
                