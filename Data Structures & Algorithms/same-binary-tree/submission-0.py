# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use a single queue to compare pairs, or two queues like you did
        queue = deque([(p, q)])
        
        while queue:
            p_node, q_node = queue.popleft()
            
            # If both are None, this branch is identical; move to next pair
            if not p_node and not q_node:
                continue
            
            # If only one is None, or values don't match, they aren't the same
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
            
            # Add children (including None) to maintain structural comparison
            queue.append((p_node.left, q_node.left))
            queue.append((p_node.right, q_node.right))
            
        return True



