class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            seen = set()
            left, count, res = 0, 0, 0
            counter = Counter()
            
            for right, num in enumerate(nums):
                if num not in seen:
                    count += 1
                    seen.add(num)
                    
                counter[num] += 1
                
                while count > k:
                    if counter[nums[left]] == 1:
                        count -= 1
                        seen.remove(nums[left])
                    counter[nums[left]] -= 1
                    left += 1
                    
                res += right - left + 1
                
            return res
        
        return atMost(k) - atMost(k-1)