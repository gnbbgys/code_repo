class Node:
    def __init__(self, name: str):
        self.left = None
        self.right = None
        self.nxt = None
        self.name = name
        
    def __str__(self):
        return self.name
    
            
"""
       G
    A      B
  C      E   F
"""
def print_queue(q):
    for item in q:
        print(f"{item[0]} : {item[1]}")
    print("XXXXXXXXXX")
    
    
def print_tree(root):
    if root is None:
        return
    
    if root.nxt:
        print(f"{root.nxt.name}")
    
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)
        
    
def bfs_link_node(root: Node) -> Node:
    if root is None:
        return root 
    
    q = []
    q.append((0, root))
    
    while q:
        print_queue(q)
        curr = q.pop(0)
        nxt_node = q[0] if q else None
        
        if nxt_node:
            if curr[0] == nxt_node[0]:
                curr[1].nxt = nxt_node[1]
                
   
        if curr[1].left:
            q.append((curr[0]+1, curr[1].left))
        if curr[1].right:
            q.append((curr[0]+1, curr[1].right))
    
    return root
            
def build_tree():
    A = Node("A")
    B = Node("B")
    G = Node("G")
    C = Node("C")
    E = Node("E")
    F = Node("F")
    
    G.left = A 
    G.right = B
    A.left = C
    B.left = E
    B.right = F
    return G
    
root = build_tree()
node = bfs_link_node(root)
print(f"XXXXXXXX {root.name}")
print_tree(node)
    
