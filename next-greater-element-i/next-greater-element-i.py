class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic =[], {}
        if not nums1:
            return []
        
        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                dic[num] = stack[-1]
            else:
                dic[num] = -1
            stack.append(num)
            
        return [dic[num] for num in nums1]