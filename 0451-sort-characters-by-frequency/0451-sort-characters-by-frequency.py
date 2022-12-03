class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        lst = sorted([(-val, key) for key, val in counter.items()])
        res = ""
        for neg, c in lst:
            res += c * (-neg)
        return res