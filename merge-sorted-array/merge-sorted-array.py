class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m+n-1, m-1
        
        while j >= 0 and nums2:
            if nums1[j] > nums2[-1]:
                nums1[i], nums1[j] = nums1[j], nums1[i]
                j -= 1
            else:
                nums1[i] = nums2.pop()
            i -= 1

        if nums2:
            m = len(nums2)
            nums1[:m] = nums2[:]
            
                
                