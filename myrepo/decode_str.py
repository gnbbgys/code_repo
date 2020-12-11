#is mirror binary tree
"""
       G
   A      A
 B      B   

"""

class Node:
    
    def __init__(self, name: str):
        self.left = None
        self.right = None
        self.name = name
        
    def __str__(self):
        return self.name
        
    def __eq__(self, other):
        print("XXX==eq==XX")
        if other is None:
            return False
            
        return self.name == other.name
        
def is_miorr_tree(node: Node) -> bool:
    
    if node is None:
        return True
    
    self_mirror = True if node.left == node.right else False
    left_mirror = is_miorr_tree(node.left)
    right_mirror = is_miorr_tree(node.right)
    
    return self_mirror and left_mirror and right_mirror

def print_tree(node: Node):
    if node is None:
        return
    
    print(node)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)

def build_tree() -> Node:
    G = Node("G")
    A = Node("A")
    A1 = Node("A")
    B = Node("B")
    B1 = Node("B")
    C = Node("C")
    C1 = Node("C")
    
    G.left = A
    G.right = A1
    A.left = B
    #A.right = C
    A1.left = B1
    #A1.right = C1
    
    return G

#root = build_tree()
#print_tree(root)
#print(is_miorr_tree(root))    

#sum of elements = n from list 
def pair_sumto_n(mylist: list, n:int) -> list:
    list.sort(mylist)
    print(mylist)
    
mylist = [0, 3, 1, 2, 5, 6, 8, 9]
pair_sumto_n(mylist, 9)
