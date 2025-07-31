class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# Build Tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

inorder(root)  # 5 10 15
