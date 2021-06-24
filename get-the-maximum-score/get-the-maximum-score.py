class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        sum1, sum2 = 0, 0
        res = 0
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                res = max(sum1, sum2) + nums1[i]
                sum1 = sum2 = res
                i += 1
                j += 1
            
        sum1 += sum(nums1[i:])
        sum2 += sum(nums2[j:])
     
        return max(sum1, sum2)%(10**9 +7)
                