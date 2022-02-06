class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.ct = [0] * size
        self.flag = 0
        self.ones = 0
        #print(bin(self.sets)[2:].zfill(size), bin(self.mask)[2:].zfill(size))

    def fix(self, idx: int) -> None:
        if (not self.flag and not self.ct[idx]) or (self.flag and self.ct[idx]):
            self.ct[idx] = 1 - self.ct[idx]
            self.ones += 1
            #print("fix", self.ct, self.flag, self.ones)
        
         
        #print("fix",idx, self.sets, self.mask, bin(self.sets)[2:].zfill(self.size))

    def unfix(self, idx: int) -> None:
        if (not self.flag and self.ct[idx]) or (self.flag and (not self.ct[idx])):
            self.ct[idx] = 1- self.ct[idx]
            self.ones -= 1
            #print("unfix", self.ct, self.flag)
        #print("unfix", self.sets,  bin(self.sets)[2:].zfill(self.size))

    def flip(self) -> None:
        self.flag = 1- self.flag
        self.ones = self.size- self.ones
        #print("flip", bin(self.sets)[2:])
        #print("flip", self.flag)

    def all(self) -> bool:
        #print("all",self.ct, all(x == 1 for x in self.ct))
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones 

    def count(self) -> int:
        #print("count", self.ct)
        
        return self.ones

    def toString(self) -> str:
        ct_f = "".join([str(1-x) for x in self.ct])
        ct = "".join([str(x) for x in self.ct])
        return ct_f if self.flag else ct
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()