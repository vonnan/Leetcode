class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])
        res = 0
        while boxTypes and truckSize:
            num, units = boxTypes.pop()
            if num <= truckSize:
                res += num * units
            else:
                return res + truckSize * units
            truckSize -= num
        return res