class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        n, m = len(nums1), len(nums2)
        if 6* m < n or 6 * n < m:
            return -1
        
        if sum1== sum2:
            return 0
        
        diff = abs(sum1 - sum2)
        
        if sum1 < sum2:
            lst_gain = [6 - x for x in nums1]
            lst_lose = [x - 1 for x in nums2]
            
        else:
            lst_gain = [6 - x for x in nums2]
            lst_lose = [x - 1 for x in nums1]
            
        lst = [ x for x in lst_gain+ lst_lose]
        lst.sort(reverse = 1)
        
        res = 0
        for num in lst:
            diff -= num
            res += 1
            if diff <= 0:
                return res
            
        return 0
            
        