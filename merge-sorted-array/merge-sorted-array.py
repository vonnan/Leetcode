class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m ==0:
            nums1[:] = nums2
        if nums2:
            i = m + n - 1
            j = m-1
            print(i, j)
            while i >=0 and j >=0 and nums2:
                print(i, j, nums1[j], nums2[-1])
                if nums1[j] <= nums2[-1]:
                    nums1[i] = nums2.pop()
                else:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
                    if j > 0:
                        j -= 1
                    elif j ==0:
                        nums1[j] = nums2.pop()
                i -= 1
