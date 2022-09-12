class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = 1)
        odd = [num for num in nums if num % 2]
        even =[ num for num in nums if num % 2 == 0]
        
        res = sum(nums[:k])
        print(nums, res)
        if not odd or (res %2 ==0):
            return res
        
        else:
            if k == len(nums) or not even:
                return -1
            
            ct = sum(num % 2  for num in nums[:k] )
            
            if k - ct == len(even):
                if not even:
                    return -1
                else:
                    return res - even[-1] + odd[ct]
            
            else:
                if ct == len(odd):
                    return res - odd[-1] + even[k - ct]
                else:
                    if k > ct:
                        return max(res - odd[ct - 1] + even[k - ct], res - even[k - ct -1] + odd[ct])
                    else:
                        return res - odd[ct - 1] + even[k - ct]
            
        
    