from heapq import heappush
from heapq import heappop


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        tails = defaultdict(list)
        
        for num in nums:
            if tails[num - 1]:
                heappush(tails[num], heappop(tails[num -1]) + 1)
            else:
                heappush(tails[num], 1)
        
        return all(num >= 3 for val in tails.values() for num in val)