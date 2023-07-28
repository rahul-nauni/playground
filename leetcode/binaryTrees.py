# Understanding the binary trees
# For reference -> https://youtu.be/76dhtgZt38A
from __future__ import annotations
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
    
    def __repr__(self) -> str:
        return f'Node({self.val})'
    
    def get_parent(self, root, node) -> TreeNode:
        if root is None or node is None:
            return None
        while root:
            if root.left == node or root.right == node:
                return root
            elif root.left:
                return self.get_parent(root.left, node)
            elif root.right:
                return self.get_parent(root.right, node)
            else:
                return None

    
    def subtree_first(self, node) -> TreeNode:
        if node is None:
            return
        
        while node.left:
            node = node.left
        return node
    
    def subtree_last(self, node) -> TreeNode:
        if node is None:
            return
        
        while node.right:
            node = node.right
        return node
    
    def inorder_successor(self, node) -> TreeNode:
        if node.right:
            return self.subtree_first(node.right)
        else:
            return self.get_parent(self, node)
        
root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')
root.left.right = TreeNode('e')
root.left.left.left = TreeNode('f')

print(root.subtree_first(root.left))
print(root.subtree_last(root.left))
print(root.get_parent(root, root.left.left))
print(root.inorder_successor(root))
