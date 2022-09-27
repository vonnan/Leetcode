from bisect import bisect
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        lst = list(accumulate(costs))
        return bisect(lst, coins)
        