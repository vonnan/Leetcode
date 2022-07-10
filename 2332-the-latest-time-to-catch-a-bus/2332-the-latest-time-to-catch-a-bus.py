class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], A: List[int], capacity: int) -> int:
        buses.sort()
        A.sort()
        curr = 0
        n = len(A)
        for bus in buses:
            cap = capacity
            while A and cap > 0 and curr < n and A[curr] <= bus:
                cap -= 1
                curr += 1
            
        
        best = A[curr - 1] if cap==0 else bus
        print(cap, curr, best)
        sets = set(A)
        
        for b in range(best, 0, -1):
            if b not in sets:
                return b
        
        
