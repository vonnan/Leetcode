class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        
        return sum(counter[jewel] for jewel in jewels)