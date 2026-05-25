# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True,0]
            left = dfs(root.left)
            right = dfs(root.right)
            l = left[1]
            r = right [1]

            return [left[0] and right[0] and abs(l - r) <= 1, 1 + max(l,r)]
            
        return dfs(root)[0]
        

    



