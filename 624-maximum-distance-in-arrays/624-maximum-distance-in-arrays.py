class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lst = [(a[0], a[-1], r) for r, a in enumerate(arrays)]
        
        first, second = sorted(lst), sorted(lst, key = lambda x: x[1])
        
        min_ = first[0][0]
        print(first, second)
        if second[-1][-1] == first[0][-1]:
            return max(abs(second[-2][1] - min_), abs(second[-1][1] - first[1][0]))
        else:
            return second[-1][1] - min_