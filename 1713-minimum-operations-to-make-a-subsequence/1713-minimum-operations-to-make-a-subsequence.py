from bisect import bisect_left
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        dic = {c: i for i, c in enumerate(target)}
        arr = [dic[a] for a in arr if a in dic]
        if not arr:
            return n
        
        lst = [arr[0]]
        for num in arr[1:]:
            idx = bisect_left(lst, num)
            if idx != len(lst):
                lst[idx] = num
            else:
                lst.append(num)
        
        return n - len(lst)