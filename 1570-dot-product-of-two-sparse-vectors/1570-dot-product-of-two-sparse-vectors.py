class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        A, B = self.dic, vec.dic
        return sum(a * b for a, b in zip(A, B))

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)