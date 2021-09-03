class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxLst, minLst = [nums[0]], [nums[0]]
        maxSum, Sum, minSum = nums[0], nums[0], nums[0]
        for i, num in enumerate(nums[1:],1):
            maxLst.append(max(maxLst[-1], 0) + num)
            minLst.append(min(minLst[-1], 0) + num)
            maxSum = max(maxSum, maxLst[-1])
            minSum = min(minSum, minLst[-1])
            Sum += num
        print(maxLst, minLst)
        return max(maxSum, Sum - minSum) if maxSum > 0 else maxSum