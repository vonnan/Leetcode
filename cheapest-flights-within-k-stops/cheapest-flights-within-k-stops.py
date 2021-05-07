from collections import defaultdict
from heapq import heappop
from heapq import heappush
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
 
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for flight in flights:
            if flight[0] in graph:
                graph[flight[0]][flight[1]] = flight[2]
            else:
                graph[flight[0]] = {flight[1]:flight[2]}
        
        rec = {}
        heap = [(0, -1, src)]
        heapq.heapify(heap)
        while heap:
            cost, stops, city = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops == K or rec.get((city, stops), float('inf')) < cost:
                continue
            if city in graph:
                for nei, price in graph[city].items():
                    summ = cost + price
                    if rec.get((nei, stops+1), float('inf')) > summ:
                        rec[(nei, stops+1)] = summ
                        heapq.heappush(heap, (summ, stops+1, nei))
        return -1