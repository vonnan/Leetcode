class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)
        if len(s) <k:
            return False
        return  sum(x % 2 for x in counter.values())<= k
        