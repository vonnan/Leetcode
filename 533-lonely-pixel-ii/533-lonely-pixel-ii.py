class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        row, col = len(picture), len(picture[0])
        set_r, ban_c, dic, dic_c = set([]), set([]), defaultdict(list), defaultdict(set)
        
        for r in range(row):
            if picture[r].count("B") == target:
                set_r.add(r)
            for c in range(col):
                if c in ban_c:
                    continue
                if picture[r][c] == "B":
                    dic[c].append(r)
                    if r not in set_r or len(dic[c]) > target :
                        ban_c.add(c)
        
        
        res = 0
        for r in range(row):
            for c in range(col):
                if r in set_r and len(dic[c]) == target and c not in ban_c and picture[r][c] == "B":
                    dic_c[c].add("".join(picture[r]))
                    
                    
                    
        return target * sum(len(dic_c[c])== 1 for c in dic_c)