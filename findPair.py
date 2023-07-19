class Node:
    def __init__(self, val, left, right):
        self.val =  val
        self.left = None
        self.right = None

def in_order_traversal(node, sorted_array):
    if node:
        in_order_traversal(node.left, sorted_array)
        sorted_array.append(node.val)
        in_order_traversal(node.right, sorted_array)

def find_pair(root, k):
    # perform in-order traversal to get sorted array
    sorted_array = []
    in_order_traversal(root, sorted_array)

    # Initialize pointers
    left = 0
    right = len(sorted_array) - 1 

    # search for pair with sum equal to k
    while left < right:
        curr_sum = sorted_array[left] + sorted_array[right]
        if curr_sum == k:
            return sorted_array[left], sorted_array[right]
        elif curr_sum < k:
            left +=1
        else:
            right -= 1

    # no pair found
    return None

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(11)
root.right.right = Node(15)

# Set target
k = 20

pair = find_pair(root, k)
if pair:
    node1, node2 = pair
    print(f"Nodes with sum {K}: {node1} and {node2}")
else:
    print("No pair of nodes found with the given sum.")