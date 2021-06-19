class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n= len(nums)
        a = [0] * (n + 2)
        b = [0] * (n + 2)
        def insert(b, l, r, c):
            b[l] += c
            b[r+1] -= c
        
        for l,r in requests:
            insert(b, l, r, 1)
            
        for i in range(1, n+1):
            b[i] += b[i-1]
            
        b.sort(reverse = 1)
        nums.sort(reverse = 1)
        res, mod = 0, 10**9 + 7
        for i in range(n):
            res += b[i]* nums[i]
            
        return res % mod