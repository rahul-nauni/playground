class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



"""def isSameTree(p, q):
    if p is None and q is None:
        return p == q
    elif p is not None or q is not None:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)"""

def isSameTree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p is not None or q is not None and p.val == q.val:
        if p.left is None and q.left is None and p.right is None and q.right is None:
            return True
        elif p.left is not None and q.left is not None and p.right is None and q.right is None:
            return isSameTree(p.left, q.left)
        elif p.left is None and q.left is None and p.right is not None and q.right is not None:
            return isSameTree(p.right, q.right)
        elif p.left is not None and q.left is not None and p.right is not None and q.right is not None:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


p = TreeNode()
#p.left = TreeNode(2)
#p.right = TreeNode(3)

q = TreeNode(1)
#q.left = TreeNode(2)
#q.right = TreeNode(3)

print(isSameTree(p, q))