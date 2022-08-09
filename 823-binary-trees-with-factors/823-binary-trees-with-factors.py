class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        tree = defaultdict(int)
        arr.sort()
        
        res = 0
        mod = 10** 9 + 7
        
        for a in arr:
            tree[a] = sum(tree[num]* tree[a//num]  for num in arr if a % num == 0) + 1
            res += tree[a]
        
        return res % mod