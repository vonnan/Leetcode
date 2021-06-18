from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [str(i) for i in range(1, n+1)]
        return "".join(list(permutations(lst))[k-1])
        