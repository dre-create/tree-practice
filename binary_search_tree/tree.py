
class TreeNode: 
    def __init__(self, key, value = None):
        if value == None:
            value = key

        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add_helper(self, current, key, value):
        if not current:
            return TreeNode(key,value)
        if key <= current.key:
            current.left = self.add_helper(current.left,key,value)
        else:
            current.right = self.add_helper(current.right,key,value)
        return current


    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def add(self, key, value = None):
        if self.root == None:
            self.root = TreeNode(key,value)
        else:
            self.add_helper(self.root, key,value)

        
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def find(self, key):
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorder(self):
        tree_nodes = []
        return self.inorder_helper(self.root, tree_nodes)

    def inorder_helper(self, root, tree_nodes):
        if root:
            self.inorder_helper(root.left, tree_nodes)
            tree_nodes.append({
                "key":root.key,
                "value":root.value
            })
            self.inorder_helper(root.right, tree_nodes)
        return tree_nodes


    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def preorder(self):
        tree_nodes = []
        return self.preorder_helper(self.root, tree_nodes)

    def preorder_helper(self, root, tree_nodes):
        if root:
            tree_nodes.append({
                "key":root.key,
                "value":root.value
            })
            self.preorder_helper(root.left, tree_nodes)
            self.preorder_helper(root.right, tree_nodes)
        return tree_nodes



    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def postorder(self):
        tree_nodes = []
        return self.postorder_helper(self.root, tree_nodes)

    def postorder_helper(self, root, tree_nodes):
        if root:
            self.postorder_helper(root.left, tree_nodes)
            self.postorder_helper(root.right, tree_nodes)
            tree_nodes.append({
                "key":root.key,
                "value":root.value
            })
        return tree_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(h)    
    def height(self):
        return self.height_helper(self.root)
    
    def height_helper(self, current):
        if not current:
            return 0

        left = self.height_helper(current.left)
        right = self.height_helper(current.right)
        return max(left, right)+1

        


#   # Optional Method
#   # Time Complexity: 
#   # Space Complexity: 
    def bfs(self):
        pass

        


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"


