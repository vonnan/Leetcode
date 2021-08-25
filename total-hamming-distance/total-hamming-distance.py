class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        nums = [bin(num)[2:].zfill(32) for num in nums]
        
        res = 0
        for i in range(32):
            bits =[0, 0]
            for num in nums:
                
                bits[int(num[i])] += 1
            res += bits[0] * bits[1]
        return res
            
            
        