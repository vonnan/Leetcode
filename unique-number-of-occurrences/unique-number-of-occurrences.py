class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lst = list(Counter(arr).values())
        return len(lst) == len(set(lst))