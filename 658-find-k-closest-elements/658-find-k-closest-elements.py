class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted([(abs(a - x), a) for a in arr])
        return sorted([a for _, a in arr[:k]])
        