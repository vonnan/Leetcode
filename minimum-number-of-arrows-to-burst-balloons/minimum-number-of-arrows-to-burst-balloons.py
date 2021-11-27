class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return len(points)
        
        points.sort()
        
        end = points[0][1]
        count = 1
        
        for s,e in points[1:]:
            
            if s <= end:
                
                end = min(e, end)
            else:
                count += 1
                end = e
                
        return count
                
            
        