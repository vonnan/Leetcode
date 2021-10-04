class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower -1] + nums +[upper + 1]
        
        stack = []
        
        for i, num in enumerate(nums[:-1]):
            if nums[i + 1] <= nums[i] + 1:
                continue
            elif nums[i + 1] == nums[i] + 2:
                stack.append(str(num + 1))
            else:
                stack.append(str(num + 1) + "->" + str(nums[i+1] - 1))
                
        return stack