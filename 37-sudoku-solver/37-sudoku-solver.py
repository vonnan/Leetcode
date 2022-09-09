class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = {'1','2','3','4','5','6','7','8','9'}
        boxNums = defaultdict(set)  # type: Dict[Set[int]]
        rowNums = defaultdict(set)  # type: Dict[Set[int]]
        colNums = defaultdict(set)  # type: Dict[Set[int]]
        dots = []
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    dots.append((r, c))
                else:
                    boxNums[(r // 3, c // 3)].add(val)
                    rowNums[r].add(val)
                    colNums[c].add(val)
        
        dotCount = len(dots)
        
        def solve(i: int = 0) -> bool:
            if i >= dotCount:
                return True
            
            r, c = dots[i]
            br = r // 3
            bc = c // 3
            available = nums - boxNums[(br, bc)] - rowNums[r] - colNums[c]
            
            if not available:
                return False
            
            for n in available:
                board[r][c] = n
                boxNums[(br, bc)].add(n)
                rowNums[r].add(n)
                colNums[c].add(n)
                if solve(i+1):
                    return True
                
                boxNums[(br, bc)].remove(n)
                rowNums[r].remove(n)
                colNums[c].remove(n)
            
        solve()
        