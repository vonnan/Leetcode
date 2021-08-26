class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        bits = 1
        
        for row in mat:
            temp = 0
            for num in row:
                temp |= bits << num
            bits = temp
            
        for x in range(5000):
            if bits >> (target + x) & 1 or x < target and bits >> (target - x) & 1:
                return x