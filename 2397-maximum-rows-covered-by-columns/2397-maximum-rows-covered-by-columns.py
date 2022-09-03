from itertools import combinations
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        row, col = len(mat), len(mat[0])
        dic = defaultdict(set)
        
        for r, rows in enumerate(mat):
            for c in range(col):
                if mat[r][c] == 1:
                    dic[r].add(c)
        
        res = 0
        print(dic)
        for x in combinations(range(col), cols):
            ct = 0
            x = set(x)
            
            for r in range(row):
                if len(dic[r]) > cols:
                    continue
                if not dic[r]:
                    ct += 1
                elif dic[r] & x == dic[r]:
                    ct += 1
            print(x, ct)
            res = max(res, ct)
        return res
                
                    
                