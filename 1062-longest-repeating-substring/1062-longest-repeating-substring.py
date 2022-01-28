class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        counter = Counter(s)
        sets = [key for key, val in counter.items() if val == 1 ]
        n = len(s)
        dic = defaultdict(int)
        res = 0
        for i,c in enumerate(s):
            if c in sets:
                continue
            for j in range(i+1, n):
                if s[j] in sets:
                    break
                if s[i:(j+ 1)] not in dic:
                    dic[s[i:(j + 1)]] = i
                else:
                    if i > dic[s[i: (j+ 1)]]:
                        res = max(res, j - i + 1)
        return res
                
        
        
