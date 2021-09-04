class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        lst = [[]]
        for i, num in enumerate(nums):
            if num >0:
                lst[-1].append(1)
            elif num <0:
                lst[-1].append(-1)
            elif lst[-1] !=[]:
                lst.append([])
        res = 0
        print(lst)
        for num in lst:
            if not num:
                continue
            n = len(num)
            if num.count(-1) % 2 == 0:
                res = max(res, n)
            else:
                res = max(res, n - 1 - min(num.index(-1), num[::-1].index(-1)))
                
        return res
            
                
            