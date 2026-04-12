# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        if not root: return res

        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                cur_node = q.popleft()
                if cur_node.left: q.append(cur_node.left)
                if cur_node.right: q.append(cur_node.right)

        return res         