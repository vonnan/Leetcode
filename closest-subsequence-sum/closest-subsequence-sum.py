from sortedcontainers import SortedList
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        set1, set2 = set([0]), set([0])
        n = len(nums)
        for i, num in enumerate(nums[:n//2]):
            set1 |= {prev + num for prev in set1}
            
        for i, num in enumerate(nums[n//2:]):
            set2 |= {prev + num for prev in set2}
        
        lst1, lst2 = sorted(set1), sorted(set2)
        n1, n2 = len(lst1), len(lst2)
        res = inf
        l, r = 0, n2-1
        while l < n1 and r >=0:
            temp = lst1[l] + lst2[r] 
            if temp == goal:
                return 0
            res = min(res, abs(temp - goal))
            if temp < goal:
                l += 1
            else:
                r -= 1
        return res
        
        
            
            
        
        
        
        
        