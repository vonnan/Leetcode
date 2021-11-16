
class Solution:
    
    def nthUglyNumber(self, n: int) -> int:
        q = deque([1])
        for _ in range(n - 1):
            min_ = q[-1] * 2
            while q[0] * 5 <= q[-1]:
                q.popleft()
            for prod in set([2,3,5]):
                for x in q:
                    if min_ > x * prod > q[-1]:
                        min_ = x * prod
            q.append(min_)
        return q[-1]