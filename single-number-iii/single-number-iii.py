class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        diff = xor & (-xor)
        
        right_one = 0
        for num in nums:
            if num & diff:
                right_one ^= num
        
        return [right_one, right_one^xor]