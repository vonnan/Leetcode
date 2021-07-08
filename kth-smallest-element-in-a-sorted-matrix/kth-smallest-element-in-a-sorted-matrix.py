class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = sorted([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))])
        return lst[k-1]
        