# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        count2 = 0
        ans = [0]
        

        def dfs2(root):
            nonlocal count2
            nonlocal ans
            if not root:
                return

            dfs2(root.left)
            count2+= 1
            if count2 == k:
                ans[0] = root.val
            dfs2(root.right)
        dfs2(root)
        return ans[0]





        

    
        