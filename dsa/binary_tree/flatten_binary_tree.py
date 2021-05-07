from bst import BST

def get_nodes_in_order(node, array):
    if node is None:
        return
    get_nodes_in_order(node.left, array)
    array.append(node)
    get_nodes_in_order(node.right, array)

def faltten_tree(array):
    for i in range(0, len(array)-1):
        left_node = array[i]
        right_node = array[i+1]
        
        left_node.left = None
        left_node.right = right_node
        
        right_node.left = left_node
        right_node.right = None
    
    return array[0]

if __name__ == '__main__':
    root = BST()
    items = [2, 3, 1, 5, 4, 6, 7]
    for i in items:
        root.add_node(i)

    array = []
    get_nodes_in_order(root, array)

    for node in array:
        print(node.data)
    
    node = faltten_tree(array)
    while node is not None:
       print(node.data)
       node = node.right


    