class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
       
        for _ in range((n-1)% 14 + 1):
        
            
            res = [0]  + [1- cells[j-1] ^ cells[j+1] for j in range(1, 7)] + [0]
            cells = res[:]
            
        return res
            