class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        lst = sorted(list(counter.values()))
        target = n - n//2
        
        res = 0
        while target >0:
            target -= lst.pop()
            res += 1
        return res