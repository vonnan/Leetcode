class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = len(tasks)
        counter = Counter(tasks)
        max_ = max(counter.values())
        m = sum(val == max_ for val in counter.values())
        return max(t, (max_ - 1) * (n + 1) + m)
        