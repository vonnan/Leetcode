class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > n *k or target < n:
            return 0
        
        prev = {i : 1 for i in range(1, k + 1)}
        mod = 10 **9 + 7
        for _ in range(n - 1):
            curr = defaultdict(int)
            for i in range(1, k + 1):
                for key, val in prev.items():
                    if key + i <= target:
                        curr[key + i] += val
                        curr[key + i] %= mod
            
            prev = curr.copy()
        return prev[target]
                        
