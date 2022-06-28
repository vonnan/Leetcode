class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        counter_r, counter_c = defaultdict(int),defaultdict(int)
        row, col = len(picture), len(picture[0])
        sets = set([(r,c) for r in range(row) for c in range(col) if picture[r][c] == "B"])
        print(len(sets))
        for r,c in sets:
            counter_r[r] += 1
            counter_c[c] += 1
        
        return sum((counter_r[r] == 1 and counter_c[c] == 1) for r,c in sets)
            
                
                
                