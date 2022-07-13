class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def ct_0(num):
            if num == 0:
                return 0
            return num//5 + ct_0(num//5)
        
        left, right = 0, 5*k  + 1
        while left < right:
            mid = (left + right)//2
            val = ct_0(mid)
            if val == k:
                return 5
            elif val < k:
                left = mid + 1
            else:
                right = mid
        
        return 0
                 