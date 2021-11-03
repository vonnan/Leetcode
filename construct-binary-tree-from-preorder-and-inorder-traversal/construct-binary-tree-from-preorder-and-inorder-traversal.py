# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            val = preorder.pop(0)
            idx = inorder.index(val)
            node = TreeNode(val)
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx + 1:])
            return node
            
            