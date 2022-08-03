class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def helper(start):
            seen = []
            sets = set([])
            
            while start not in sets:
                seen.append(start)
                sets.add(start)
                start += nums[start]
                start %= n
        
            if seen[-1] == start:
                return False
        
            num = nums[start]
            while seen[-1] != start:
                if nums[seen.pop()] * num <0:
                    return False
            return True
        
        return any(helper(start) for start in range(n))
            
                