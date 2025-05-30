# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

# Build tree manually
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder: ", end="")
inorder(root)     # 4 2 5 1 3
print("\nPreorder: ", end="")
preorder(root)    # 1 2 4 5 3
print("\nPostorder: ", end="")
postorder(root)   # 4 5 2 3 1
