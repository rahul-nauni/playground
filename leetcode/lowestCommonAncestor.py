from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f'{self.val}'
    

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]) -> TreeNode:
        if not root:
            return None

        # If the root is one of the nodes, return the root
        if root in nodes:
            return root
        # traverse left and right subtrees 
        # checking if any of the nodes are present
        # If one of the subtrees doesn't contain any given node, 
        # the LCA can be the node returned from the other subtree
        # If both subtrees contain nodes, the LCA node is the current node.
        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)
         
        if left and right:
            return root
        
        return left if left else right


    

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

nodes = [TreeNode(4), TreeNode(7)]

s = Solution()
print(s.lowestCommonAncestor(root, nodes))