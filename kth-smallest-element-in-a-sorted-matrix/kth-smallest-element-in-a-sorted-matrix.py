from bisect import insort
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = matrix[0]
        n = len(matrix)
        for r in range(1, len(matrix)):
            for c in range(n):
                insort(lst, matrix[r][c])
        return lst[k-1]