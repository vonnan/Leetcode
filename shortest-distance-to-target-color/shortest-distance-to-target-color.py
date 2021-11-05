from bisect import bisect_left

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dp = [[], [], []]
        for i, c in enumerate(colors):
            dp[c-1].append(i)
            
        res = []
        for idx, c in queries:
            c -= 1
            if not dp[c]:
                res.append(-1)
                continue
            index = bisect_left(dp[c], idx)
            if index == len(dp[c]):
                res.append(idx - dp[c][-1])
            elif index == 0:
                res.append(dp[c][0] - idx)
            else:
                res.append(min(dp[c][index] - idx, idx - dp[c][index -1]))
        
        return res
                
            
        