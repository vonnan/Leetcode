class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = [ x+ 1 for x in nums1], [x + 1 for x in nums2]
        sets = set(nums1) & set(nums2)
        if not sets:
            return 0
        
        h = 128
        set1 = set2 = sets
        max_ = 1
        for i, c in enumerate(nums1):
            if c not in sets:
                continue
            pre = c
            
            for j, d in enumerate(nums1[i+1:], i + 1):
                if d not in sets:
                    break
                pre = h * pre + d
                if pre not in set1:
                    set1.add(pre)
            
        for i, c in enumerate(nums2):
            if c not in sets:
                continue
            pre = c
            for j, d in enumerate(nums2[i+1:], i + 1):
                if d not in sets:
                    break
                pre = h * pre + d
                if pre in set1:
                    if pre > max_:
                        max_ = pre
                        
                else:
                    break
        
        res = 0
        while max_:
            max_ = max_//h
            res += 1
        return res
                
            
