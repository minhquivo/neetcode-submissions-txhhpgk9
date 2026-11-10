"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        old_to_new = {} 
        old_to_new[node] = Node(node.val)
        q = deque() 
        q.append(node)

        while q: 
            cur = q.popleft() 
            for neigh in cur.neighbors: 
                if neigh not in old_to_new: 
                    old_to_new[neigh] = Node(neigh.val) 
                    q.append(neigh)
                old_to_new[cur].neighbors.append(old_to_new[neigh])
        
        return old_to_new[node]