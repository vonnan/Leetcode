from heapq import merge
from heapq import heappop

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        heap = (merge(nums1, nums2))
        heap = list(heap)
        n = len(heap)
        if n %2:
            return heap[n//2]
        else:
            return (heap[n//2 -1] + heap[n//2])/2
        
            
       
        
                
            