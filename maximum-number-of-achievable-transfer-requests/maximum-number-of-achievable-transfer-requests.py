class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        m = len(requests)
        for mask in range(1, 1 <<m):
            dic = defaultdict(int)
            ct = 0
            for i in range(m):
                if mask & (1 <<i):
                    u, v = requests[i]
                    dic[u] -= 1
                    dic[v] += 1
                    ct += 1
            if all(val ==0 for val in dic.values()):
                res = max(res, ct)
        return res
                
                    