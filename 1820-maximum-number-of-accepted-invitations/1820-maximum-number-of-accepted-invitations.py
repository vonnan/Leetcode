class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        matches = [-1] * col
        
        def dfs(node, seen):
            for c in range(col):
                if grid[node][c] and not seen[c]:
                    seen[c] = True
                    if matches[c] == -1 or dfs(matches[c], seen):
                        matches[c] = node
                        return True
            return False
        
        res = 0
        
        for r in range(row):
            seen = [False] * col
            if dfs(r, seen):
                res += 1
        
        return res
                
                    
