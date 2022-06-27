class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = 0
        for key, val in counter.items():
            if key + 1 in counter:
                res += val
        
        return res
                