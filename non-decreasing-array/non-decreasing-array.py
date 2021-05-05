class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if p != None:
                    return False
                else:
                    p = i
                    
        if p == None or (p ==0) or (p ==len(nums) -2) or (nums[p-1] <= nums[p+1]) or (nums[p] <= nums[p+2]):
            return True
        else:
            return False
                    
                    
                    
             