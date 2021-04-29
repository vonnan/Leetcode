from collections import defaultdict
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        nums.sort(reverse = 1)
        dic = defaultdict(int)
        tot = defaultdict(int)
        
        for num in nums:
            a, b , c = num//100, num//10 % 10, num%10
            dic[(a,b)] = max(1, dic[(a+1, 2*b -1)] + dic[(a+1, 2*b)])
            tot[(a,b)] = tot[(a+1, 2*b -1)] + tot[(a+1, 2*b)] + dic[(a,b)] * c
        
        return tot[(1,1)]