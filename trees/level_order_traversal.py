from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque()
    q.append(root)
    traversal_list = []

    while q:
        size = len(q)
        level_list = []
        for _ in range(size):
            node = q.popleft()
            level_list.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        traversal_list.append(level_list)

    return traversal_list

if __name__ == "__main__":
    # root = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print(levelOrderTraversal(root))
