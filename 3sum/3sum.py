class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, res = len(nums), set([])
        
        for i, num in enumerate(nums[:-2]):
            target = -num
            l, r = i + 1, n-1
            if 2 * nums[r] <target:
                continue
            if 2 * nums[l] > target:
                break
            while l < r:
                x = nums[l] + nums[r]
                if x == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif x > target:
                    r -= 1
                else:
                    l += 1
        return res