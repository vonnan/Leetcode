class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        leftsubTree, minsubTree =[], -inf
        
        for num in preorder:
            if num < minsubTree:
                return False
            while leftsubTree and num > leftsubTree[-1]:
                minsubTree = leftsubTree.pop()
                
            leftsubTree.append(num)
            
        return True
        