class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        lst = sorted([(-val, key) for key, val in counter.items()])
        print(lst)
        return [key for _, key in lst[:k]]