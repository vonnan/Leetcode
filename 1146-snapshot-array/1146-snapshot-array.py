from bisect import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.size = length
        self.array = {i: [[-1, 0]] for i in range(self.size)}
        self.id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect(self.array[index], [snap_id, inf])
        return self.array[index][idx - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)