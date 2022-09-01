class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        for i in range(n):
            if sensor1[i] != sensor2[i]:
                break
        if i == n -1 or (sensor1[i:-1] == sensor2[i + 1:] and sensor2[i:-1] == sensor1[i + 1:]):
            return -1
        if sensor1[i:-1] == sensor2[i + 1:]:
            return 1
        else:
            return 2
        