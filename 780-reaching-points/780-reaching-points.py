class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty== sy:
                return True
            
            if tx == ty:
                return False
            
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx ) % sy == 0
            
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % sx == 0
        
        return False
                        
            
            