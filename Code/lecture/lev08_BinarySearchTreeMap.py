class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

        def disconnect(self): #function purpose?
            self.item = None
            self.left = None
            self.right = None
            self.parent = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count
    
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.Item.key
    
    def is_empty(self):
        return self.size == 0
    
    def find_node(self, key):
        curr = self.root
        while(curr is not None):
            if(curr.item.key == key):
                return curr
            elif(curr.item.key > key):
                curr = self.left
            elif(curr.item.key < key):
                curr = self.right
        return None #if key was not found in the tree
    
    def __getitem__(self, key):
        node = self.find_node(key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value
        
    def __setitem__(self, key, value):
        node = self.find_node(key)
        if (node is None):
            self.insert(key, value)
        else:
            node.item.value = value


    def insert(self, key, value):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if(self.is_empty):
            self.root = new_node
            self.size=1
        else:
            parent = self.root
            if (key < parent.item.key):
                curr = parent.left
            else:
                curr = parent.right
            #run the sarch until curr reaches None
            while(curr is not None):
                parent = curr
                if(key < parent.item.key): #how exactly does the while constraint check happen here 
                    curr = parent.left
                else:
                    curr = parent.right
            #new node should be chld of parent
            new_node.parent = parent
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node

            self.size += 1
    
    def __delitem__(self, key):
        node = self.find_node(key)
        if (node is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.delete_node(node)

    def delete_node(self, node_to_delete):
        item = node_to_delete.item
        num_children = node_to_delete.num_children()

        if(node_to_delete is self.root):

            if(num_children == 0): #deleting the last node!
                self.root = None
                node_to_delete.disconnect()
                self.size = 0
            elif (num_children == 1):
                if (node_to_delete.right is None):
                    self.root = node_to_delete.left
                else:
                    self.root = node_to_delete.right

                self.size -= 1
                self.root.parent = None
            else:
                min_of_right = self.subtree_min(node_to_delete.right)
                node_to_delete.item = min_of_right.item
                self.delete_node(min_of_right)
        else:
            if (num_children == 0):
                parent = node_to_delete.parent

                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (node_to_delete.left is None): #copy and delete child (method A demonstrated for left)
                    node_to_delete.item = node_to_delete.right.item
                    node_to_delete.left = node_to_delete.right.left
                    node_to_delete.right = node_to_delete.right.right
                    node_to_delete.right.disconnect()

                    if(node_to_delete.left is not None):
                        node_to_delete.left.parent = node_to_delete
                    if(node_to_delete.right is not None):
                        node_to_delete.right.parent = node_to_delete

                else: #redirect parent to child (method B demonstrated for right)
                    parent = node_to_delete.parent
                    if (parent.left == node_to_delete):
                        parent.left = node_to_delete.left
                    else:
                        parent.right = node_to_delete.left

                    node_to_delete.left = parent
                    node_to_delete.disconnect()
                self.size -= 1
            else: #two children
                min_of_right = self.subtree_min(node_to_delete.right)
                node_to_delete.item = min_of_right.item
                self.delete_node(min_of_right)

    def subtree_min(self, curr):
        while(curr.left is not None):
            curr = curr.left
        return curr
    
    def inorder(self):
        def subtree_inorder(root):
            if(root is None):
                pass #nothin to do!
            else:
                yield subtree_inorder(root.left)
                yield root
                yield subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def __iter__(self):
        for node in self.inorder():
            yield self.item.key

def main():
    bst = BinarySearchTreeMap()
    for i in range(10):
        bst[random.randint(1, 100)]=0

    for key in bst:
        print(key)

if __name__=='__main__':
    main()



        

        


        