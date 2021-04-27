class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_node(self, data):
        if data == self.data:
            return
        
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
    
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()  
        print(self.data)
        if self.right:
            self.right.in_order_traversal()
    
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
    
    def is_node_exists(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.is_node_exists(value)
            else:
                False

        if value > self.data:
            if self.right:
                return self.right.is_node_exists(value)
            else:
                False
    
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
        


if __name__ == '__main__':
    root = BST(3)
    root.add_node(1)
    root.add_node(4)
    root.add_node(5)
    root.add_node(9)
    root.add_node(8)

    print("Pre Order Traversal")
    root.pre_order_traversal()
    print("In Order Traversal")
    root.in_order_traversal()
    print("Post Order Traversal")
    root.post_order_traversal()

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
    root.delete_node(5)

    print("In order traversal after node deletion")
    root.in_order_traversal()

    root.delete_node(1)
    root.delete_node(8)
    root.delete_node(4)
    root.in_order_traversal()