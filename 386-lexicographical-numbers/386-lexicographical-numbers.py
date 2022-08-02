class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        x = sorted([(str(num), num) for num in range(1, n + 1)])
        return [ num for _, num in x]