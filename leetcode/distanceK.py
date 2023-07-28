from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertToGraph(self, root):
        adjList = {}
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr.val not in adjList:
                adjList[curr.val] = []
            
            if curr.left:
                adjList[curr.val].append(curr.left.val)
                if curr.left.val not in adjList:
                    adjList[curr.left.val] = []
                adjList[curr.left.val].append(curr.val)
                queue.append(curr.left)
            if curr.right:
                adjList[curr.val].append(curr.right.val)
                if curr.right.val not in adjList:
                    adjList[curr.right.val] = []
                adjList[curr.right.val].append(curr.val)
                queue.append(curr.right)
            
        return adjList
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # error checking
        if root is None or target is None:
            return []
        if k == 0:
            return [target.val]
        
        # convert tree to graph
        adjList = self.convertToGraph(root)
        
        # BFS from target node
        result = []
        depth = 0
        visited = set()
        queue = deque()
        queue.append(target.val)
        while queue:
            if depth > k:
                break
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr not in visited:
                    visited.add(curr)
                    for neighbor in adjList[curr]:
                        queue.append(neighbor)
                    if depth == k:
                        result.append(curr)
            depth += 1
                         
        # return nodes at distance k
        return result

s = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6) 
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
target = TreeNode(5)
k = 2

print(s.distanceK(root, target, k))


