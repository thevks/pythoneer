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
