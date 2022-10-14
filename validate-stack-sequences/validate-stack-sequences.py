class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        for num in pushed:
            if popped[0] != num:
                stack.append(num)
            else:
                popped.pop(0)
                while stack and popped and stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
        return not popped
        
                