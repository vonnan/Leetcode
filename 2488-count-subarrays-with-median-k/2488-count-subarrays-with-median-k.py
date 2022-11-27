class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if k not in nums:
            return 0
        idx = nums.index(k)
        
        res = []
        for i, num in enumerate(nums):
            if num == k: res.append(0)
            elif num > k: res.append(1)
            else: res.append(-1)
                
        presum = list(accumulate(res))
        
        counter_f, counter_b = Counter([0] + presum[:idx]), Counter(presum[idx:]), 
        res  =  0
        
        for front, val in counter_f.items():
            if front in counter_b:
                res += val * counter_b[front]
            if front + 1 in counter_b:
                res += val * counter_b[front + 1]
        
        return res
                