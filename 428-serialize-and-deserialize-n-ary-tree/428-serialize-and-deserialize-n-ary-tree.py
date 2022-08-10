"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
        def dfs(node, lst):
            if not node:
                return lst
            
            lst.append(node.val)
            for child in node.children:
                lst.append(dfs(child, []))
            return lst
        
        return dfs(root, [])
            
            
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        def dfs(lst):
            if not lst:
                return None
            
            root = Node(lst[0], [])
            for x in lst[1:]:
                root.children.append(dfs(x))
            return root
        
        return dfs(data)
            
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))