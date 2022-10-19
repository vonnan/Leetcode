from bisect import bisect
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        target = n //2
        counter = Counter(arr)
        lst = sorted(list(counter.values()))
        
        lst = list(accumulate(lst))
        idx = bisect(lst, target)
        return len(lst) - idx
        