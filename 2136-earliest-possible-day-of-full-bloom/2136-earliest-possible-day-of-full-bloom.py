class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        lst = sorted([(b, a) for a,b in zip(plantTime, growTime)], reverse = True)
        print(lst)
        plant, grow = [p for _, p in lst], [ g for g, _ in lst]
        
        prefix = list(accumulate(plant))
        
        res = prefix[-1]
        for i, g in enumerate(grow):
            res = max(res, prefix[i] + g)
        
        return res