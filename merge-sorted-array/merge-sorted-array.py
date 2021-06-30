class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lst = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                lst.append(nums1[i])
                i += 1
            else:
                lst.append(nums2[j])
                j += 1
                
        lst += nums1[i:m] + nums2[j:n]
        
        nums1[:] = lst
                
        