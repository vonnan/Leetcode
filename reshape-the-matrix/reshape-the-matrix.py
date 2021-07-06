class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(nums), len(nums[0])
        lst = [nums[x][y] for x in range(row) for y in range(col)]
        
        if len(lst) != r*c:
            return nums
        else:
            l = []
            idx = 0
            while idx < c*r:
                l.append(lst[idx:idx+c])
                idx += c
            return l
                
                