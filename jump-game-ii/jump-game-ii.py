class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        last = n-1
        reach =[i + num for i, num in enumerate(nums)]
        
        while last > 0:
            flag = False
            for i in range(last):
                if reach[i] >= last:
                    flag = True
                    last = i
                    break
            res += 1
        return res