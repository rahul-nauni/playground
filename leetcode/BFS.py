class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
    def __repr__(node):
        return node.val
    
    def bfs(root):
        if root is None:
            return []
        
        queue = [root]
        result = []
        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    
node = Node('a')
node.left = Node('b')
node.right = Node('c')
node.left.left = Node('d')
node.left.right = Node('e')
node.right.right = Node('f')

print(node.left)
print(node.bfs())
