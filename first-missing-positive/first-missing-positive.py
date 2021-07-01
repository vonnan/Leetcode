class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sets = set()
        counter = Counter()
        max_num = 0
        for num in nums:
            if num >0:
                sets.add(num)
                counter[num] = 1
                max_num = max(max_num, num)
        
        for i in range(1, max_num+1):
            if i not in counter:
                return i
        
        return max_num + 1
        
        