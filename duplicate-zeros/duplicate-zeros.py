class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr[:] = [ x for a in arr for x in ([a] if a else [0, 0])][:len(arr)]