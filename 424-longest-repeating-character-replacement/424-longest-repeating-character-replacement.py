class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_, start = 0, 0
        counter = Counter()
        for end, c in enumerate(s):
            counter[c] += 1
            max_ = max(max_, counter[c])
            while max_ + k < end - start + 1:
                counter[s[start]] -= 1
                start += 1
        return len(s) - start