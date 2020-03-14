class TreeNode:  # This is the Class TreeNode with constructor that contains data variable to type data and left,right pointers.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createBinaryTree(inputList):
    """通过一个列表生成二叉树
    
    :inputList: 一个列表，按层序遍历顺序包含生成二叉树所需的数据，空值为None
    :rtype: TreeNode
    """
    if not inputList:
        return None
    data = inputList.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = createBinaryTree(inputList)
    node.right = createBinaryTree(inputList)
    return node

def preOrderTraveral(tree):   # Pre order traveral of the tree
    
    if tree is None:
        return
    
    print(tree.data)
    preOrderTraveral(tree.left)
    preOrderTraveral(tree.right)
    
    return
    
def inOrderTraveral(tree):  # In Order traveral of the tree

    if tree is None:
        return

    inOrderTraveral(tree.left)
    print(tree.data)
    inOrderTraveral(tree.right)

    return

def postOrderTraveral(tree):  # Post Order traveral of the tree

    if tree is None:
        return

    postOrderTraveral(tree.left)
    postOrderTraveral(tree.right)
    print(tree.data)

    return

def depth_of_tree(
    tree,
):  # This is the recursive function to find the depth of binary tree.
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


def is_full_binary_tree(
    tree,
):  # This functions returns that is it full binary tree or not?
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return False


def main():  # Main func for testing.
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.left.right.left = TreeNode(6)
    tree.right.left = TreeNode(7)
    tree.right.left.left = TreeNode(8)
    tree.right.left.left.right = TreeNode(9)

    t = createBinaryTree([1,2,4,None,None,5,6,None,None,None,3,7,8,None,9])
    
    print('\n')
    postOrderTraveral(t)
    print('\n')
    
    
    # print(is_full_binary_tree(tree))
    # print(depth_of_tree(tree))
    # print("Tree is: ")
    # inOrderTraveral(tree)


if __name__ == "__main__":
    main()
