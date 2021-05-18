class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        lst = [0] * (max(nums) + 1)
        for num in counter:
            for i in range(num, len(lst), num):
                lst[i] += counter[num]
        linear = list(accumulate(lst))
        mod = 10**9 + 7
        return sum(linear[num] for num in nums) % mod
                
            