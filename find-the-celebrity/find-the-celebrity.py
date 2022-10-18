# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        
        for j in range(n):
            if j == celebrity:
                continue
            if knows(celebrity, j) or not knows(j, celebrity):
                return -1
        
        return celebrity
            