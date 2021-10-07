class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            two = A[l] + A[r]
            if two == target:
                return (l + 1, r + 1)
            
            elif two < target:
                l += 1
                
            else:
                r -= 1
                
                