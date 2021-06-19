from collections import defaultdict
class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.array = [0]*(self.n+1)
        for i in range(self.n):
            self.helper(i,nums[i])

    def helper(self,i, val):
        n = self.n
        i += 1
        while i<=n:
            self.array[i] += val
            i += i&(-i)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.helper(i,val-self.nums[i])
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum_i = self.get_sum(i-1)
        sum_j = self.get_sum(j)
        return sum_j-sum_i
        
    def get_sum(self,i):
        
        s = 0
        i += 1
        while i>0:
            s += self.array[i]
            i -= i&(-i)
        return s
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)