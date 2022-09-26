from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.SL = SortedList()
        self.k = k 
        for num in nums:
            self.SL.add(num)

    def add(self, val: int) -> int:
        self.SL.add(val)
        
        return self.SL[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)