class SnapshotArray:

    def __init__(self, length: int):
        self.snapid = 0
        self.arr = defaultdict(dict)
        self.size = length
        
        
    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snapid] = val
        
    def snap(self) -> int:
        for index in self.arr:
            if self.snapid in self.arr[index]:
                self.arr[index][self.snapid + 1] = self.arr[index][self.snapid]
        self.snapid += 1
        return self.snapid - 1
 
    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.arr[index]:
            return self.arr[index][snap_id]
        else:
            return 0
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)