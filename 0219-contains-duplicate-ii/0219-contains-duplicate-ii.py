class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = i
            elif  i - dic[num] > k:
                dic[num] = i
            else:
                return True
        return False
                
        
        