from bisect import bisect
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        left, right = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        while left < right:
            mid = (left + right)//2
            if sum(bisect(nums2, mid - num) for num in nums1) <k:
                left = mid + 1
            else:
                right = mid
        res = []
        for num in nums1:
            if num + nums2[0] > left:
                break
            m = bisect(nums2, left - num)
            for j in range(m):
                res.append([num, nums2[j]])
        res.sort(key = lambda x: x[0] + x[1])
        return res[:k]
                
    
       
                    
        