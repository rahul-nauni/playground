# Depth First Search

# root -> left -> right
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(node):
        return node.val

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def dfs_by_iteration(node):
    stack = [node]
    result = []
    while len(stack) > 0:
        current = stack.pop() # keep track of current node
        result.append(current.val)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result

def dfs_by_recurssion(node):
    if node is None:
        return []
    leftVals = dfs_by_recurssion(node.left)
    rightVals = dfs_by_recurssion(node.right)

    return [node.val] + leftVals + rightVals

def main():
    result = dfs_by_iteration(a)
    print(result)

if __name__ == "__main__":
    main()