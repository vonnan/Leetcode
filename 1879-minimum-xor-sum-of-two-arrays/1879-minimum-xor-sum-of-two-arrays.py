class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @lru_cache(None)
        def dp(mask, r):
            if r == n:
                return 0
            
            return min(dp(mask ^ (1 << c), r + 1) + (nums1[r] ^ nums2[c]) for c in range(n) if mask & (1 << c) )
        
        return dp((1<<n)-1, 0)