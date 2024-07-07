class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 10
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
    
    
    
#different approach

class bTree:
    def __init__(self,data):
        self.data = data  
        self.left = None
        self.right = None
        
    def pre_orderTraversal(self,Node): 
        result= []
        def helper(Node):
            if Node is None:
                return
            result.append(Node.data)
            helper(Node.left)
            helper(Node.right)   
        helper(Node) 
        print(result)
                   


root = bTree('R')  
nodeA = bTree('A')
nodeB = bTree('B')
nodeC = bTree('C')
nodeD = bTree('D')
nodeE = bTree('E')
nodeF = bTree('F')
nodeG = bTree('G')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
#print("root.right.left.data:", root.right.left.data)


# Array implementation of Tree
binary_tree_array =  ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']


def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def get_data(index):
    if 0<= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None 

def inorder_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return inorder_traversal(left_child_index(index)) + [binary_tree_array[index]] + inorder_traversal(right_child_index(index)) 

def preorder_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return   [binary_tree_array[index]] +  preorder_traversal(left_child_index(index))+ preorder_traversal(right_child_index(index))   

def postorder_traversal(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return   postorder_traversal(left_child_index(index)) + postorder_traversal(right_child_index(index)) + [binary_tree_array[index]] 

right_child = right_child_index(0)
left_child_of_right_child = left_child_index(right_child)
data = get_data(left_child_of_right_child)       