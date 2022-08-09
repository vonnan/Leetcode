class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def top(nums, n):
            res = []
            remove = len(nums) - n
            for num in nums:
                while remove and res and res[-1] < num:
                    res.pop()
                    remove -= 1
                res.append(num)
            return res[:n]
        
        def merge(lst1, lst2):
            return [max(lst1, lst2).pop(0) for _ in (lst1 + lst2)]
        
        return max(merge(top(nums1, i), top(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and (k-i)<= len(nums2))
        
                