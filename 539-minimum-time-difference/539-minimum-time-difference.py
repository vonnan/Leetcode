class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        A =[time.split(":")  for time in timePoints]
        A= [ int(time[0]) * 60 + int(time[1]) for time in A]
        A.sort()
        n = len(A)
        return min(min(A[i+1] - A[i] for i in range(n-1)), A[0] + 24* 60 -A[-1])