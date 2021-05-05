class BST:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    
    def add_node(self, data):
        if self.data is None : 
            #Special case, when root is empty
            self.data = data
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
    
    def _get_min_value(self) :
        if self.left is None :
            return self.data
        else :
            self.left._get_min_value()
    
    def remove_node(self, value, parent = None):
        if value < self.data:
            if self.left is not None :
                self.left.remove_node(value, self)
        elif value > self.data:
            if self.right is not None :
                self.right.remove_node(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.data = self.right._get_min_value()
                self.right.remove_node(self.data, self)            
            elif parent is None: #Node is root of tree
                if self.left is None and self.right is None :
                    self = None
                elif self.left is not None:
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
    
    def nodes_count(self) :
        if self is None or self.data is None :
            return 0
        left_count = 0
        if self.left :
            left_count = self.left.nodes_count()
        right_count = 0
        if self.right :
            right_count = self.right.nodes_count()
        return 1 + left_count + right_count
    
    def pre_order_traversal(self) :
        if self is None :
            return
        print(self.data)
        if self.left :
            self.left.pre_order_traversal()
        if self.right :
            self.right.pre_order_traversal()
                
    def in_order_traversal(self, values) :
        if self is None:
            return values          
        if self.left : 
            self.left.in_order_traversal(values)
        values.append(self.data)
        if self.right :
            self.right.in_order_traversal(values)
        return values

    def post_order_traversal(self) :
        if self is None:
            return
        if self.left :
            self.left.pre_order_traversal()
        if self.right :
            self.right.pre_order_traversal()
        print(self.data)
  
if __name__ == '__main__' :
    root = BST()
    #nums = [3, 1, 4, 5, 9, 8]
    nums = [3, 1, 4]
    for num in nums :
        root.add_node(num)

    #print("Pre Order Traversal")
    #root.pre_order_traversal()
    print("In Order Traversal before deletion : ")
    print(root.in_order_traversal([]))
    #print("Post Order Traversal")
    #root.post_order_traversal()
    #print("Number of nodes before deletion: %d", root.nodes_count())
    
    #for num in nums :
    #    root.remove_node(num)    
    
    #print("In Order Traversal after deletion : ")
    #print(root.in_order_traversal([]))
    
    print("Number of nodes after deletion: %d", root.nodes_count())

    root.remove_node(3)
    print(root.in_order_traversal([]))
    root.remove_node(1)
    print(root.in_order_traversal([]))
    root.remove_node(4)
    print(root.in_order_traversal([]))
