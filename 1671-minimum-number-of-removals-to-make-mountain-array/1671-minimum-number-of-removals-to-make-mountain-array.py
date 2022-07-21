from bisect import bisect_left
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lst, left, right = [nums[0]], [0], [0]
        
        for num in nums[1:]:
            idx = bisect_left(lst, num)
            n = len(lst)
            left.append(idx)
            if idx == n:
                lst.append(num)
            else:
                lst[idx] = num
        
        lst = [nums[-1]]
        for num in nums[::-1][1:]:
            idx = bisect_left(lst, num)
            n = len(lst)
            right.append(idx)
            if idx == n:
                lst.append(num)
            else:
                lst[idx] = num
        
        right = right[::-1]
        
        return len(nums) -max(a + b + 1 for a, b in zip(left, right) if a and b)