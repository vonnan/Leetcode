class MKAverage:
    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.arr = [0]*m
        self.lh1, self.rh1 = self.heap_init(m, k)
        self.lh2, self.rh2 = self.heap_init(m, m - k)
        self.score = 0
        
    def heap_init(self, p1, p2):
        h1 = [(0, i) for i in range(p1-p2, p1)]
        h2 = [(0, i) for i in range(p1-p2)]
        heapq.heapify(h1)
        heapq.heapify(h2)
        return (h1, h2)
        
    def update(self, lh, rh, m, k, num):
        score, T = 0, len(self.arr)
        if num > rh[0][0]:
            heappush(rh, (num, T))        
            if self.arr[T - m] <= rh[0][0]:
                if rh[0][1] >= T - m: score += rh[0][0]
                score -= self.arr[T - m]
                heappush(lh, (-rh[0][0], rh[0][1]))
                heappop(rh)
        else:
            heappush(lh, (-num, T))       
            score += num
            if self.arr[T - m] >= rh[0][0]: 
                heappush(rh, (-lh[0][0], lh[0][1]))
                q = heappop(lh)
                score += q[0]
            else:
                score -= self.arr[T - m]

        while lh and lh[0][1] <= T - m: heappop(lh)  # lazy-deletion
        while rh and rh[0][1] <= T - m: heappop(rh)  # lazy-deletion
        return score
        
    def addElement(self, num):
        t1 = self.update(self.lh1, self.rh1, self.m, self.k, num)
        t2 = self.update(self.lh2, self.rh2, self.m, self.m - self.k, num)
        self.arr.append(num)
        self.score += (t2 - t1)
    
    def calculateMKAverage(self):
        if len(self.arr) < 2*self.m: return -1
        return self.score//(self.m - 2*self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()