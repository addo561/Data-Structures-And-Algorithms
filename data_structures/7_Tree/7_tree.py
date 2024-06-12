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
print("root.right.left.data:", root.right.left.data)
