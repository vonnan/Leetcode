class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {i:v for i, v in enumerate(nums)}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        a, b = self.dic, vec.dic
        return sum(a[i] * b[i] for i in a)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)