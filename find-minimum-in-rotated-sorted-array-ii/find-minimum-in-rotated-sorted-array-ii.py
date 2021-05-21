class Solution:
    def findMin(self, nums: List[int]) -> int:
        sets = set(nums)
        visited = set([])
        lst = []
        
        for num in nums:
            if num not in visited:
                lst.append(num)
                visited.add(num)
        
        left, right = 0, len(lst) -1
        
        if len(lst) <=2:
            return min(lst)
        
        while left < right:
            mid = (left + right) //2
            if lst[mid] > lst[left] and lst[mid] > lst[right]:
                left = mid +1
            else:
                right = mid
            if right - left <=2:
                return min(lst[left: right + 1])

        
                