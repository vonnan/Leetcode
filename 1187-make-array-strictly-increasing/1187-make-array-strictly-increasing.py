from bisect import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Record the possible states of each position and number of operations to get this state.
When we check i-th element in the arr1, dp record the possible values we can place at this position, and the number of operations to get to this state.
Now, we need to build dp for (i+1)-th position, so for (i+1)-th element,
if it's larger than the possible state from i-th state, we have two choices:
1, keep it so no operation needs to be made.
2, choose from arr2 a smaller element that is larger than i-th element and add one operation.
If it's not larger than the i-th state, we definitely need to make a possible operation.


        """
        
        arr2 = sorted(list(set(arr2)))
        dp = {0: arr1[0], 1: arr2[0]}
        
        for i, a in enumerate(arr1[:-1]):
            new = {}
            
            for ops in dp:
                if dp[ops] < arr1[i + 1]:
                    new[ops] = min(new.get(ops, inf), arr1[i+1])
                idx = bisect(arr2, dp[ops])
                if idx == len(arr2):
                    continue
                new[ops + 1] = min(new.get(ops + 1, inf), arr2[idx])
            
            if not new:
                return -1
            dp = new
            
        return min(dp)
            
        