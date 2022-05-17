# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', TR: 'Point', BL: 'Point') -> int:        
        res = 0
        if TR.x >= BL.x and TR.y >= BL.y and sea.hasShips(TR, BL):
            if TR.x== BL.x and TR.y == BL.y:
                return 1
            
            mx, my = (TR.x + BL.x)//2, (TR.y + BL.y)//2
            
            res += self.countShips(sea, TR, Point(mx + 1, my + 1))
            res += self.countShips(sea, Point(mx, my), BL)
            res += self.countShips(sea, Point(mx, TR.y), Point(BL.x, my + 1))
            res += self.countShips(sea, Point(TR.x, my), Point(mx+1, BL.y))
        return res