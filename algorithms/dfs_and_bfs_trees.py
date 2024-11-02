class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


# Check if Value Exists (DFS) Time: O(n), Space: O(n)
def search_dfs(node, target):
  if not node:
    return False

  if node.val == target:
    return True

  return search_dfs(node.left, target) or search_dfs(node.right, target)

# Time: O(log n), Space: O(log n)
def search_bfs(node, target):
  if not node:
    return False

  if node.val == target:
    return True

  if target < node.val: return search_bfs(node.left, target)
  else: return search_bfs(node.right, target)



  
# Iterative Pre Order Traversal (DFS) Time: O(n), Space: O(n)
def pre_order_iterative(node):
  stk = [node]

  while stk:
    node = stk.pop()
    if node.right: stk.append(node.right)
    if node.left: stk.append(node.left)
    print(node)
    
    
# Level Order Traversal (BFS) Time: O(n), Space: O(n)
from collections import deque

def level_order(node):
  q = deque()
  q.append(node)

  while q:
    node = q.popleft()
    print(node)
    if node.left: q.append(node.left)
    if node.right: q.append(node.right)      
  