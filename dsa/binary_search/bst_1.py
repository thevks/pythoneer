class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_node(self, data):
        if data < self.data:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = BST(data)
        #return self
    
    def find_kth_smallest(self, k):
        sorted_array = []
        _in_order_traversal(self, sorted_array)
        return sorted_array[k-1]

    def find_kth_largest(self, k):
        sorted_array = []
        _in_order_traversal(self, sorted_array)
        return sorted_array[len(sorted_array) - k]

    def in_order_traversal(self):
        sorted_array = []
        self._in_order_traversal(sorted_array)

    def _in_order_traversal(self, sorted_array):
        if self is None:
            return
        self.left._in_order_traversal(sorted_array)  
        print(self.data)
        sorted_array.append(self.data)
        self.right._in_order_traversal(sorted_array)
    
    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()
        print(self.data)
    
 
    def contains(self, value):           
        if value < self.data:
            if self.left:
                return self.left.contains(value)
            else:
                False
        elif value > self.data:
            if self.right:
                return self.right.contains(value)
            else:
                False
        else:
            return True
    
    def find_maximum_node(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_maximum_node()

    def find_minimum_node(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_minimum_node()

    def sum_of_all_nodes(self):
        left_sum = self.left.sum_of_all_nodes() if self.left else 0
        right_sum = self.right.sum_of_all_nodes() if self.right else 0
        return self.data + left_sum + right_sum
    
    def find_closest_node(self, target):
        current_node = self
        closest = self.data 
        while current_node is not None:
            if abs(target - closest) > abs(target - current_node.data):
                closest = current_node.data
            if target < current_node.data:
                current_node = current_node.left
            elif target > current_node.data:
                current_node = current_node.right
            else:
                break
        return closest

    def _search_node(self, value):
        found = False
        q = self
        parent = None
        current = None

        while q is not None:
            if q.data == value:
                found = True
                current = q
                break
            elif q.data > value:
                parent = q
                q = q.left
            else:
                parent = q
                q = q.right
        
        return parent, current, found

    def delete_node(self, value):
        if (self == None):
            print("Tree is empty")
            return
        
        parent, current, found = self._search_node(value)

        if found is False:
            print("Node is not found")
            return

        #Case 1: Node to be deleted has two children
        if current.left is not None and current.right is not None:
            parent = current
            xsucc = current.right

            while xsucc.left is not None:
                parent = xsucc
                xsucc = xsucc.left
            
            current.data = xsucc.data
            current = xsucc
        
        #Case 2: Node to be deleted has only right child
        if current.left is None and current.right is not None:
            if parent.left is current:
                parent.left = current.right
            else:
                parent.right = current.right
                            
        #Case 3: Node to be deleted has only left child
        elif current.left is not None and current.right is None:
            if parent.left is current:
                parent.left = current.left
            else:
                parent.right = current.right
                        
        #Case 4: Node to be deleted has no children
        elif current.left is None and current.right is None:
            if parent.left is current:
                parent.left = None
            else:
                parent.right = None
        
        print("Node is deleted in delete_node function ")
        return

    def _get_min_value(self):
        if self.left is None:
            return self.data
        else:
            self.left._get_min_value()

    def remove_node(self, value, parent = None):
        if value < self.data:
            if self.left is not None:
                self.left.remove_node(value, self)
        elif value > self.data:
            if self.right is not None:
                self.right.remove_node(value, self)
        else:
            if self.left is not None and self.self.right is not None:
                self.data = self.right._get_min_value()
                self.right.remove_node(self.data, self)
            elif parent is None:
                if self.left is not None:
                    self.data = self.left.data
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.data = self.right.data
                    self.left = self.right.left
                    self.right = self.right.right
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.right if self.right is not None else self.left
        return self

def print_paths_and_branch_sum(node, stack, paths):
         
    if node is None :
        return
        
    stack.append(node.data)
        
    if node.left is None and node.right is None :
        print("Sum of path ", stack, "--> ", sum(stack))
        paths.append(stack)
        return
                    
    print_paths_and_branch_sum(node.left, stack, paths)            
    print_paths_and_branch_sum(node.right, stack, paths)

    stack.pop()

def branchSums(node, runninSum, sums) :
    if node is None :
        return
    
    newRunningSum = runninSum + node.data
    
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    
    branchSums(node.left, newRunningSum, sums)
    branchSums(node.right, newRunningSum, sums)


def depths_sum(node, depth) :
    if node is None :
        return 0
    
    return (depth + depths_sum(node.left, depth+1) + 
                    depths_sum(node.right, depth+1))

def depths_sum_v2(root):
    sum = 0
    stack = [{"node":root, "depth": 0}]

    while stack:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        sum += depth
        stack.append({"node" : node.left, "depth" : depth + 1})
        stack.append({"node" : node.right, "depth" : depth + 1})
    
    return sum

def nodes_count(node) :
    if node is None :
        return 0
    elif node.left is None and node.right is None :
        return 1
    else :
        return 1 + nodes_count(node.left) + nodes_count(node.right)

def _is_bst_valid(node, min_value, max_value):
    if node is None:
        return True
    
    if (node.data < min_value or node.data > max_value) :
        return False
    
    return (_is_bst_valid(node.left, min_value, node.data) and
           _is_bst_valid(node.right, node.data, max_value)) 

def is_bst_valid(root) :
    return _is_bst_valid(root, float("-inf"), float("inf"))

def copy_tree(root):
    if root is None:
        return
    new_root = BST(root.data)
    new_root.left = copy_tree(root.left)
    new_root.right = copy_tree(root.right)
    
    return new_root

def mirror_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)

def height(node):
    if node is None :
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)

"""
left_height + right_height +1 is the diameter through the tree's root
max(left_diameter, right_diameter) is the max of each side's diameter, 
i.e. when the longest path does not pass through the binary tree's root.
    
The diameter can occur through:
    1) The binary tree's root, meaning that its longest path is from the 
    left subtree through the root and down into the right subtree.
    2) The left or right subtree without passing through the binary tree's root.
"""
def diameter(node):
    if node is None :
        return 0
    
    left_height = height(node.left)
    right_height = height(node.right)
    
    left_diameter = diameter(node.left)
    right_diameter = diameter(node.right)
 
    return max(left_height + right_height + 1, max(left_diameter, right_diameter))

def is_bst_height_balanced(node) :
    if node is None:
        return True
    
    left_height = height(node.left)
    right_height = height(node.right)

    if abs(left_height - right_height) > 1 :
        return False
    
    return is_bst_height_balanced(node.left) and is_bst_height_balanced (node.right)

def is_balanced(node) :
    if node is None:
        return True
    
    left_height = height(node.left)
    right_height = height(node.right)

    if (abs(left_height - right_height) <= 1 and
        is_balanced(node.left) is True and
        is_balanced(node.right) is True) :
        return True
    
    return False

def find_path(root, value, path) :
    """
    Function to find path from root to node
    """
    if root is None :
        return False

    path.append(root.data)

    if (root.data == value) :
        return True
    
    if ((find_path(root.left, value, path)) or                                                   
        (find_path(root.right, value, path))) :
        return True
    
    path.pop()
    return False

def find_common_ancestor(root, n1, n2) : 
    path1 = []
    path2 = []

    if (not find_path(root, n1, path1) or
        not find_path(root, n2, path2)) :
        return -1
    
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    
    print("Common ancestor of {} & {} is {}".format(n1, n2, path1[i-1]))
    return path1[i-1]

def sameBSTs(aL1, aL2):
      
    # Base cases
    if (len(aL1) != len(aL2)):
        return False
    if (len(aL1) == 0):
        return True
    if (aL1[0] != aL2[0]):
        return False
      
    # Construct two lists from each input array. The first
    # list contains values smaller than first value, i.e.,
    # left subtree. And second list contains right subtree.
    aLLeft1 = []
    aLRight1 = []
    aLLeft2 = []
    aLRight2 = []
    for i in range(1, len(aL1)):
        if (aL1[i] < aL1[0]):
            aLLeft1.append(aL1[i])
        else:
            aLRight1.append(aL1[i])
          
        if (aL2[i] < aL2[0]):
            aLLeft2.append(aL2[i])
        else:
            aLRight2.append(aL2[i])
    
    # Recursively compare left and right
    # subtrees.
    return sameBSTs(aLLeft1, aLLeft2) and sameBSTs(aLRight1, aLRight2)


def check_descendent(root, n1, n2) :
    """
    Function should return True, if n2 is descendent of n1
    else False

    Start iterating on tree using n1, if n2 exists down the tree return True, else return False
    """

def check_ascendent(root, n1, n2) :
    """
    Function should return True, if n2 is ascendent of n1
    else False

    Start iterating on tree using n2, if n1 exists down the tree return True, else return False
    """

def leaf_to_leaf_paths(node):
    pass

  
if __name__ == '__main__':
    root = BST(3)
    root.add_node(1)
    root.add_node(4)
    root.add_node(5)
    root.add_node(9)
    root.add_node(8)

    print("Pre Order Traversal")
    root.pre_order_traversal()
    #print("In Order Traversal")
    #root.in_order_traversal()
    #print("Post Order Traversal")
    #root.post_order_traversal()

    print("Sum of nodes ", root.sum_of_all_nodes())

    print("Min of Node ", root.find_minimum_node())
    print("Max of Node ", root.find_maximum_node())

    print("Closest node of 6 ", root.find_closest_node(6))
    print("Closest node of 15 ", root.find_closest_node(15))
    print("Closest node of 65 ", root.find_closest_node(65))

    parent_node, matched_node, found = root._search_node(5)
    if found is True:
        print("Node 5 is found with: ")
        print("Parent Node", parent_node.data)
        print("Matched Node", matched_node.data)
    else:
        print("Node 5 not found")

    print("Going to delete node 5")
    #root.delete_node(5)

    print("In order traversal after node deletion")
    #root.in_order_traversal()

    #root.remove_node(8)
    #root.in_order_traversal()

    print("Print Paths")    
    paths = []
    print_paths_and_branch_sum(root, [], paths)
    print(paths)

    #sums = []
    #branchSums(root, 0, sums)
    #print(sums)

    print("Nodes Count : ")
    print(nodes_count(root))

    print("Depth Sums : ")
    print(depths_sum(root, 0))
    
    print("Depth Sums V2 : ")
    print(depths_sum_v2(root))

    print(is_bst_valid(root))

    #print("2nd Largest: ", root.find_kth_largest(2))
    #print("2nd smallest: ", root.find_kth_smallest(2))

    mirror_tree(root)
    print("Mirror Copy: ")
    root.pre_order_traversal()

    new_root = copy_tree(root)
    print("Copy of Tree: ")
    new_root.pre_order_traversal()

    print("Diameter of tree : ")
    print(diameter(new_root))

    print(is_bst_height_balanced(new_root))
    print(is_balanced(new_root))

    path = []
    if find_path(new_root, 7, path) is True :
        print("Path is found: ")
    else:
        print("Path is not found: ")
    
    print(path)

    
    find_common_ancestor(new_root, 1, 8)
    find_common_ancestor(new_root, 1, 5)
    find_common_ancestor(new_root, 3, 4)
    find_common_ancestor(new_root, 8, 9)
    find_common_ancestor(new_root, 3, 8)


    aL1 = []
    aL2 = []
    aL1.append(3)
    aL1.append(5)
    aL1.append(4)
    aL1.append(6)
    aL1.append(1)
    aL1.append(0)
    aL1.append(2)
    
    aL2.append(3)
    aL2.append(1)
    aL2.append(5)
    aL2.append(2)
    aL2.append(4)
    aL2.append(6)
    aL2.append(0)

    if sameBSTs(aL1, aL2) :
        print("BSTs are same: ")
    else :
        print("BSTs are not same: ")