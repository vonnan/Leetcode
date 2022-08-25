from math import ceil

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n = len(people)
        left, right = 0, n - 1
        res = 0
        while left < right:
            if people[right] * 2 <= limit:
                return res + ceil((right - left + 1)/2)
            elif people[right] + people[left] <= limit:
                right -= 1
                left += 1
                res += 1
            else:
                right -= 1
                res += 1
        
        if left == right:
            res += 1
        
        return res
            
            
            
            