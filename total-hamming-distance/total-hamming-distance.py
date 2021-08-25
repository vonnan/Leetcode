class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        nums =[bin(num)[2:].zfill(32) for num in nums]
        res = 0
        for i in range(32):
            zero, one = 0, 0
            for num in nums:
                if num[i] == "0":
                    zero += 1
                else:
                    one += 1
            res += one * zero
        return res
            
                    
                    