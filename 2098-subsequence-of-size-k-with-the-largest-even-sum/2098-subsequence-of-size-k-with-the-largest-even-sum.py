class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        odd = [num for num in nums if num % 2]
        even =[ num for num in nums if num % 2 == 0]
        if k == 1:
            if not even:
                return -1
            return even[-1]
        
        res = sum(nums[-k:])
        
        if not odd or (res %2 ==0):
            return res
        
        else:
            if k == len(nums) or not even:
                return -1
            
            ct = sum(num % 2  for num in nums[-k:] )
            
            if k - ct == len(even):
                if not even:
                    return -1
                else:
                    return res - even[0] + odd[-(ct + 1)]
            
            else:
                if ct == len(odd):
                    return res - odd[-ct] + even[-(k - ct + 1)]
                else:
                    if k > ct:
                        return max(res - odd[-ct] + even[-(k - ct + 1)], res - even[-(k - ct)] + odd[-(ct + 1)])
                    else:
                        return res - odd[-ct] + even[-(k - ct + 1)]
            
        
    