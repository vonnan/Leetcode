class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        grid = set(["".join([str(x) for x in row]) for row in grid])
        if len(grid) > 2:
            return False
        elif len(grid) == 1:
            return True
        
        else:
            first, second = grid.pop(), grid.pop()
            if str(int(first) + int(second)) == "1" * len(first):
                return True
            return False
        
        