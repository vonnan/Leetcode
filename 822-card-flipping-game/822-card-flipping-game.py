class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        sets = set([a for a, b in zip(fronts, backs) if a == b])
        counter = Counter(fronts) + Counter(backs)
        for key in sorted(counter.keys()):
            if key not in sets:
                return key
        return 0