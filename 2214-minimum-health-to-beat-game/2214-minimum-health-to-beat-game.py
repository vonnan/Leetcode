from bisect import bisect_left
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        damage.sort()
        idx = bisect_left(damage, armor)
        tot = sum(damage)
        n = len(damage)
        if idx == n:
            return tot - damage[-1] + 1
        else:
            return tot - armor + 1