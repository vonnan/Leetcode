from bisect import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        heaters =[-inf] + heaters +[inf]
        i = 1
        radius = 0
        for house in houses:
            while house > heaters[i]:
                i += 1
            radius = max(radius, min(house - heaters[i-1], heaters[i] -  house))
        return radius
                         
        
        