class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)
        
        nums1.sort()
        nums2 = sorted([(num, i) for i, num in enumerate(nums2)])
        res = [0] * len(nums1)
        
        while nums2:
            last, idx = nums2.pop()
            if nums1[-1] > last:
                res[idx] = nums1.pop()
            else:
                res[idx] = nums1.pop(0)
        
        return res
                