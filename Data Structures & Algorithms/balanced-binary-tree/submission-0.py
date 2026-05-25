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
                return [0,True]
            left,leftFlag = dfs(root.left)
            right,rightFlag = dfs(root.right)

            flag = leftFlag and rightFlag and  not abs(left -right) > 1

            return [1 + max(left,right),flag]

        
        return dfs(root)[1]