class Node():
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
def create_binary_tree(tree_list):
    data = tree_list.pop(0)
    if data:
        node = Node(data)
        node.left_child = create_binary_tree(tree_list)
        node.right_child = create_binary_tree(tree_list)
        return node
    else:
        return None
def pre_order_Traveral(node):
    if node:
        print(node.data)
        pre_order_Traveral(node.left_child)
        pre_order_Traveral(node.right_child)
def in_order_Traveral(node):
    if node:
        in_order_Traveral(node.left_child)
        print(node.data)
        in_order_Traveral(node.right_child)
def post_order_Traveral(node):
    if node:
        post_order_Traveral(node.left_child)
        post_order_Traveral(node.right_child)
        print(node.data)
