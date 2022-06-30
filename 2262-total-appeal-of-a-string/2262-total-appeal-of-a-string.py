class Solution:
    def appealSum(self, s: str) -> int:
        
        dic = defaultdict(int)
        n = len(s)
        res = 0
        for i, c in enumerate(s):
            
            dic[c] = i + 1
            res += sum(dic.values())
        
        return res
            
            