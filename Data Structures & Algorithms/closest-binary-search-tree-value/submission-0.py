# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res= 0
        def dfs(root,target,diff):
            nonlocal res
            if not root:
                return float("INF")
            if abs(float(root.val) -float(target)) <= diff:
                diff = abs(float(root.val) -float(target))
                res = root.val
            root.left = dfs(root.left,target,diff)
            root.right = dfs(root.right,target,diff)
            return min(diff,root.left,root.right)

        dfs(root,target,abs(float(target) - float(root.val)))
        return res
        