from itertools import permutations 
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        res = set([])
        for i in range(1, n+1):
            for x in permutations(tiles, i):
                res.add("".join(x))
        return len(res)
            
        