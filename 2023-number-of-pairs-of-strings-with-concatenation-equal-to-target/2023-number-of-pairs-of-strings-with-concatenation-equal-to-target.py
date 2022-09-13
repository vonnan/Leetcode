class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[len(num)].append(i)
        m = len(target)
        res = 0
        
        for i, num in enumerate(nums):
            n = len(num)
            if num == target[:n]:
                for j in dic[m - n]:
                    if j != i and nums[j] == target[n:]:
                        res += 1
        
        return res
                
        