class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = [ i for i, num in enumerate(nums) if num ==0]
        n = len(nums)
        if len(zeros) <= k:
            return n
        
        res= max(zeros[0], n - 1- zeros[-1])
      
        
        for i in range(len(zeros)):
            left, right = i, min(len(zeros)-1, i +k -1)
            if left ==0:
                res = max(res, zeros[right + 1])
            elif right == len(zeros) - 1:
                res = max(res, n - 1 - zeros[left -1])
            else:
                res = max(res, zeros[right + 1]- zeros[left -1] - 1)
                
        return res