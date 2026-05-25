# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root,p,q):
            if not root:
                return
            # if root.val == p or root.val == q or root.val:
            
            if root.val > p and root.val > q:
                left = dfs(root.left,p,q)
                return left
            if root.val < p and root.val < q:
                right = dfs(root.right,p,q)
                return right
            if (root.val > p and root.val < q) or  (root.val > q and root.val < p) or root.val == p or root.val == q :
                return root
            




        return dfs(root,p.val,q.val)
        