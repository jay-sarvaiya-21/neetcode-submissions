# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good = 0

        stack = [root.val]
        def dfs(root):
            nonlocal good
            if not root:
                return
            if stack[-1] <= root.val:
                good+= 1
            
            stack.append(max(root.val,stack[-1]))
            
            dfs(root.left)
            
            dfs(root.right)
            stack.pop()

        dfs(root)

        return good
        