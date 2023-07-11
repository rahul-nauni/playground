# Problem: Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Problem statement: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
class TreeNode(object):    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def dfs(self, node, max_val):
        if not node or node.val is None:
            return
        if node.val >= max_val:
            self.count += 1
            max_val = node.val
        if node.left:
            self.dfs(node.left, max_val)
        if node.right:
            self.dfs(node.right, max_val)

        
    def goodNodes(self, root):
        if not root:
            return 0
        self.count = 0
        self.dfs(root, root.val)
        return self.count
    
input = [3,1,4,3,None,1,5]
root = TreeNode(input[0])
root.left = TreeNode(input[1])
root.right = TreeNode(input[2])
root.left.left = TreeNode(input[3])
root.left.right = TreeNode(input[4])
root.right.left = TreeNode(input[5])
root.right.right = TreeNode(input[6])

s = Solution()
print(s.goodNodes(root))