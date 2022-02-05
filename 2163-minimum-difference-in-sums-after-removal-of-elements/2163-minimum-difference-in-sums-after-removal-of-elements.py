from sortedcontainers import SortedList

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        m = n//3
        front = SortedList(nums[:m])
        back = SortedList(nums[m:])
        sum_front, sum_back = sum(front), sum(back[-m:])
        res = sum_front - sum_back
        
        for k, num in enumerate(nums[m:(2*m)], m):
            if num < front[-1]:
                front.add(num)
                sum_front += num - front.pop()
            
            back.remove(num)
            if num > back[-m]:
                sum_back += back[-m] - num
            
            
            res = min(sum_front - sum_back, res)
       
        return res
            
            
        
