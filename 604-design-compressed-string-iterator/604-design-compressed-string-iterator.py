class StringIterator:

    def __init__(self, compressedString: str):
        self.lst = []
        a, d = "", ""
        for c in compressedString:
            if c.isalpha():
                self.lst.append((a,d))
                a, d = c, ""
            elif c.isdigit():
                d += c
        self.lst.pop(0)
        self.lst.append((a,d))
        self.lst = self.lst[::-1]
                

    def next(self) -> str:
        if not self.lst:
            return " "
        a, d = self.lst.pop()
        if int(d) > 1:
            d = str(int(d) - 1)
            self.lst.append((a, d))
        return a
            
            
        

    def hasNext(self) -> bool:
        return self.lst


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()