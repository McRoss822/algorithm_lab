class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_node(root, value):
    if not root:
        return None
    if root.value == value:
        return root
    left_result = find_node(root.left, value)
    if left_result:
        return left_result
    else:
        return find_node(root.right, value)        

def in_order_successor(root: BinaryTree, node_value: BinaryTree) -> BinaryTree:
    successor = None
    node = find_node(root, node_value)
    if root is None:
        return None
    if node.right:
        current_successor = node.right
        if current_successor.left:
            while current_successor.left:
                current_successor = current_successor.left
        successor = current_successor
        return successor
    else:
        while node.parent:
            if node == node.parent.left:
                return node.parent
            node = node.parent
        if successor:    
            return successor.value
        else:
            return "not found(most right)"      

#     10
#    /  \
#   5    15
#  / \    \
# 3   7   20
#         /
#        12 

root = BinaryTree(10)
root.left = BinaryTree(5)
root.left.parent = root
root.right = BinaryTree(15)
root.right.parent = root
root.left.left = BinaryTree(3)
root.left.left.parent = root.left
root.left.right = BinaryTree(7)
root.left.right.parent = root.left
root.right.right = BinaryTree(20)
root.right.right.parent = root.right
root.right.right.left = BinaryTree(12)
root.right.right.left.parent = root.right.right
target_node = 7
successor = in_order_successor(root, target_node)
print(successor.value)