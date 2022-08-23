from bisect import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        lst = [(0, 0)] + sorted([(d, p) for d,p in zip(difficulty, profit)])
        dic = defaultdict(int)
        max_= 0
        for i, x in enumerate(lst):
            d, p = x
            max_ = max(max_, p)
            dic[i] = max_
          
        res = 0
        for d in sorted(worker):
            idx = bisect(lst, (d, inf)) - 1
            
            res += dic[idx]
        
        return res
            