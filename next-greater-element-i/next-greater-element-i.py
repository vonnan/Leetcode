class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = [], {}
        
        n = len(nums2)
        for i in range(n-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                dic[nums2[i]] = stack[-1]
            else:
                dic[nums2[i]] = -1
            stack.append(nums2[i])
                
        return [dic[num] for num in nums1]
            