class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        x = sorted([str(num) for num in range(1, n + 1)])
        return [ int(num) for num in x]