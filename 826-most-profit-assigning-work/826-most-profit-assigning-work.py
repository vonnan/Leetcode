from bisect import bisect
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        lst = sorted([[d, p] for d,p in zip(difficulty, profit)])
        
        dic = defaultdict(int)
        max_= 0
        dic[0] = max_
        
        for i, x in enumerate(lst):
            d, p = x
            max_ = max(max_, p)
            dic[i] = max_
        
        res = 0
        counter = Counter(worker)
        for w, val in counter.items():
            idx = bisect(lst, [w, inf]) - 1
            res += dic[idx] * val
        return res
            
            
            
        
            