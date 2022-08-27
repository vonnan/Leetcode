class SnapshotArray:

    def __init__(self, length: int):
        self.size = length
        self.array = defaultdict(dict)
        self.id = 0

    def set(self, index: int, val: int) -> None:
        self.array[self.id][index] = val

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id and index not in self.array[snap_id]:
            snap_id -= 1
        if snap_id == 0 and index not in self.array[0]:
            return 0
        return self.array[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)