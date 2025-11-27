# Вариант 16. Реализуйте три вида обхода бинарного дерева (preorder, inorder, postorder).
class TreeNode: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 
def preorder_traversal(root): 
    if root is None: 
        return 
    print(root.data, end=' ') 
    preorder_traversal(root.left) 
    preorder_traversal(root.right) 
def inorder_traversal(root): 
    if root is None: 
        return 
    inorder_traversal(root.left) 
    print(root.data, end=' ') 
    inorder_traversal(root.right) 
def postorder_traversal(root): 
    if root is None: 
        return 
    postorder_traversal(root.left) 
    postorder_traversal(root.right) 
    print(root.data, end=' ') 

# Создаем дерево вручную
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Вызываем обходы
print("Прямой обход:")
preorder_traversal(root) 

print("\nЦентрированный обход:")  
inorder_traversal(root)   

print("\nОбратный обход:")
postorder_traversal(root) 