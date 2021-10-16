class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = [], {}
        
        for num in nums2[::-1]:
            
            while stack and stack[-1] < num:
                stack.pop()
                
            if not stack:
                dic[num] = -1
                
            else:
                dic[num] = stack[-1]
                
            stack.append(num)
            
        return [dic[num] for num in nums1]
                
            
            