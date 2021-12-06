class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        dic = {0:0, 1:0}
        for p in position:
            if p %2:
                dic[1] += 1
            else:
                dic[0] += 1
        return min(dic.values())