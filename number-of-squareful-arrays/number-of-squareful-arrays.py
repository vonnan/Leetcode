class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def ifsquare(x):
            return int(x**0.5) **2 == x
        
        if len(nums) ==1:
            return 1 if ifsquare(nums[0]) else 0
        
        counter = Counter(nums)
        
        dic = {num :{x for x in counter if ifsquare(num + x)} for num in counter}
        
        def dfs(x, left = len(nums) - 1):
            counter[x] -= 1
            count = sum(dfs(y, left -1) for y in dic[x] if counter[y]) if left else 1
            counter[x] += 1
            return count
        
        return sum(map(dfs, counter))
        
        
        