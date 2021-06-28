class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot= sum(stones)
        memo = defaultdict(set)
        memo[0] = set([0])
        res = tot
        for stone in stones:
            for size in range(tot//2, 0, -1):
                for prev in memo[size-1]:
                    memo[size].add(prev + stone)
                    res = min( res, abs(tot - 2*(prev + stone)))
        return res
        