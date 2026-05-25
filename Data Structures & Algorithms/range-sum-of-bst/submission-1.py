# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.res = 0

        def dfs(root,l,h):
            
            if not root:
                return
            if l <= root.val <= h:
                self.res += root.val
            dfs(root.left,l,h)
            dfs(root.right,l,h)
            return 
        dfs(root,low,high)
        return self.res