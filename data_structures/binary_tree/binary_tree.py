"""生成二叉树、遍历二叉树"""
class Node():
    """节点类"""
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
def create_binary_tree(tree_list):
    """通过一个数组创建二叉树"""
    data = tree_list.pop(0)
    if data:
        node = Node(data)
        node.left_child = create_binary_tree(tree_list)
        node.right_child = create_binary_tree(tree_list)
        return node
    else:
        return None
def pre_order_Traveral(node):
    """先序遍历"""
    if node:
        print(node.data)
        pre_order_Traveral(node.left_child)
        pre_order_Traveral(node.right_child)
def in_order_Traveral(node):
    """中序遍历"""
    if node:
        in_order_Traveral(node.left_child)
        print(node.data)
        in_order_Traveral(node.right_child)
def post_order_Traveral(node):
    """后序遍历"""
    if node:
        post_order_Traveral(node.left_child)
        post_order_Traveral(node.right_child)
        print(node.data)
