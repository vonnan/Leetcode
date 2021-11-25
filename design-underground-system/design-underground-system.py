class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict(list)
        self.traveltime = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] =(stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, starttime = self.checkin.pop(id)
        self.traveltime[(start_station, stationName)].append(t - starttime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        n = len(self.traveltime[(startStation, endStation)])
        return sum(self.traveltime[(startStation, endStation)])/n


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)