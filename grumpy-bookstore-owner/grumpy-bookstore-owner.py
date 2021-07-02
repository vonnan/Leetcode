class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        n = len(customers)
        happy = sum(customers[i] * (1 - grumpy[i]) for i in range(n))
        curr = sum(customers[i] * grumpy[i] for i in range(k))
        res = curr
        for j in range(1, n-k+1):
            lo, hi = j, j+k-1
            curr += customers[hi] * grumpy[hi] -customers[lo-1] * grumpy[lo-1]
            res = max(res, curr)
        return res + happy
        
                
            