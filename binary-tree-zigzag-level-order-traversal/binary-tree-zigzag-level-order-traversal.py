# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue, level = [root], 0
        while queue:
            temp = []
            lst = []
            for q in queue:
                if q:
                    lst.append(q.val)
                    if q.left:
                        temp.append(q.left)
                    if q.right:
                        temp.append(q.right)
            
            if level%2 ==0:
                res.append(lst)
            else:
                res.append(lst[::-1])
            
            level += 1
            queue = temp
            
        return res
                        
                
                
        
        