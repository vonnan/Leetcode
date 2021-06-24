from collections import Counter
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def prod_table(nums):
            dic = defaultdict(int)
            n = len(nums)
            
            if n == 1:
                return dic
            
            for i in range(n-1):
                for j in range(i + 1, n):
                    dic[nums[i] * nums[j]] += 1
                    
            return dic
        
        dic1 = prod_table(nums1)
        dic2 = prod_table(nums2)
        
        return sum(dic1[n2* n2] for n2 in nums2) + sum(dic2[n1 * n1] for n1 in nums1)
                            
                        
            