from heapq import heappush
from heapq import heappop

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        presum = list(accumulate(nums, initial = 0))
        lst = []
        n = len(nums)
        for i in range(n - k + 1):
            lst.append(presum[i + k] - presum[i])
        
        print(lst)
        res = 0
        
        max_= lst[0]
        front = [max_]
        dic_f = defaultdict(int)
        dic_f[max_] = 0
        
        for i, num in enumerate(lst[1:], 1):
            if num > max_:
                dic_f[num] = i
                max_ = num
            front.append(max_)
        
        
        max_= lst[-1]
        m = len(lst)
        back = [(max_, m - 1)]
         
        for i in range(m -2, -1, -1):
            num = lst[i]
            if num >= max_:
                max_ = num
                back.append((max_, i))
            else:
                back.append(back[-1])
            
                
        back = back[::-1]
        res, max_ = [], 0
        for i in range(k, n- 2* k + 1):
            if lst[i] + front[i-k] + back[i + k][0] > max_:
                res = [dic_f[front[i-k]], i ,back[i + k][1]]
                max_ = lst[i] + front[i-k] + back[i + k][0]
                
        
        return res
            
            