class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        A = int("".join(map(str, digits))) + 1
        return map(int, list(str(A)))
        