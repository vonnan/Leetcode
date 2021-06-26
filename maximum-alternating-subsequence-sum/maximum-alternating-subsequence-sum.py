
class Solution(object):
    def maxAlternatingSum(self, A):
        return sum(max(A[i]- A[i-1],0) for i in range(1,len(A))) + A[0]