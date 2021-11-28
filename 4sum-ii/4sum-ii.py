class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        
        n = len(nums1)
        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                dic1[n1+ n2] += 1
        
        for i, n1 in enumerate(nums3):
            for j, n2 in enumerate(nums4):
                dic2[n1+ n2] += 1
        res = 0
        
        for key, val in dic1.items():
            if -key in dic2:
                res += val * dic2[-key]
        
        return res
                