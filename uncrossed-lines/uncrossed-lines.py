class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        row, col = len(nums1), len(nums2)
        
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        
        for r in range(row):
            for c in range(col):
                if nums1[r] == nums2[c]:
                    dp[r+1][c+1] = dp[r][c] + 1
                else:
                    dp[r+1][c+1] = max(dp[r+1][c], dp[r][c+1])
        return dp[-1][-1]
        
        