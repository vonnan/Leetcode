from bisect import bisect

class Solution:
    def countPairs(self, n, edges, queries):
        d, d2 = Counter(), Counter()
        for x, y in edges:
            d[x] += 1
            d[y] += 1
            d2[(min(x, y), max(x,y))] += 1
   
        d_sorted = sorted(d.values())
        d_sorted = [0]*(n - len(d_sorted)) + d_sorted

        out = []

        for Q in queries:
            ans = sum(n - bisect(d_sorted, Q - d_sorted[i]) for i in range(n))
            ans -= n - bisect(d_sorted, Q//2)
            ans = ans//2

            for x, y in d2:
                ans += (d[x] + d[y] - d2[x, y]) > Q
                ans -= (d[x] + d[y]) > Q
            out.append(ans)

        return out