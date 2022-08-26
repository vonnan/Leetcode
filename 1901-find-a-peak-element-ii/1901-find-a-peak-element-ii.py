class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        top, bottom = 0, len(mat) - 1
        while top < bottom:
            mid = (top + bottom)//2
            if max(mat[mid]) < max(mat[mid + 1]):
                top = mid + 1
            else:
                bottom = mid
        
        return [top, mat[top].index(max(mat[top]))]
                
