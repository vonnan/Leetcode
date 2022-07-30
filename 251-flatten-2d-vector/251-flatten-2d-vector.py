class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.matrix = vec
        self.res = []
        for row in vec:
            self.res.extend(row)
        
        
    def next(self) -> int:
        return self.res.pop(0)
    
        

    def hasNext(self) -> bool:
        if not self.res:
            return False
        return True
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()