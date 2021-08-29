class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
       
        if target %2 ==0 and (target//2 in dic) and (len(dic[target//2]) ==2):
            return dic[target//2]
        else:
            for num in dic:
                if target - num in dic and num * 2 != target:
                    return [dic[num][0], dic[target - num][0]]
            