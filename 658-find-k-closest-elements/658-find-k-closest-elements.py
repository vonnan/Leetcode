class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr, key = lambda a: abs(x - a))
        return sorted(arr[:k])