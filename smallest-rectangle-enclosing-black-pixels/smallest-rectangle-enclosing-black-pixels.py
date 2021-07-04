class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        row, col = len(image), len(image[0])
        lst =[(i, j) for i in range(row) for j in range(col) if image[i][j] == "1"]
        lst1 = sorted(lst)
        lst.sort(key = lambda x: x[1])
        print(lst1, lst)
        return (lst1[-1][0]- lst1[0][0] + 1) * (lst[-1][1] - lst[0][1] + 1)