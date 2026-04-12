# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res 
        q = deque([root])
        while q: 
            cur_level = []
            for i in range(len(q)):
                cur_node = q.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left: q.append(cur_node.left)
                if cur_node.right: q.append(cur_node.right)
            res.append(cur_level)
        
        return res 
