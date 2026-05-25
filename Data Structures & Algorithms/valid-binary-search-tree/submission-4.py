# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = float("-inf")
        r = float("inf")
        flag = True
        def dfs(l,root,r):
            nonlocal flag
            if not root:
                return

            
            left = dfs(l,root.left,root.val)
            right = dfs(root.val,root.right,r)

            if root.val >= r or root.val <= l:
                print("here")
                print(l,root.val,r)
                flag = False

            return root


        dfs(l,root,r)
        return flag