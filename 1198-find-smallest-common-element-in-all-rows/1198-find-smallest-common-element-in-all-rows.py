class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        row, col = len(mat), len(mat[0])
        counter = Counter()
        
        for r, rows in enumerate(mat):
            for num in rows:
                counter[num] += 1
                if r == row -1 and counter[num] == row:
                    return num
        
        return -1